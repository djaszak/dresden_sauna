import datetime

from django import forms
from django.contrib.admin import widgets
from django.utils import timezone
from django.forms.widgets import TimeInput

from .constants import SONG_CHOICES
from .models import Occupancy


class UltraDateInput(forms.DateInput):
    input_type = 'date'
    

class UltraTimeInput(TimeInput):
    input_type = 'time'


# Credits to
# https://stackoverflow.com/questions/10048249/how-do-i-determine-if-current-time-is-within-a-specified-range-using-pythons-da
def is_time_in_time_period(start_time, end_time, check_time):
    if start_time < end_time:
        return check_time >= start_time and check_time <= end_time
    # Over midnight
    else:
        return check_time >= start_time or check_time <= end_time


class OccupancyForm(forms.ModelForm):
    occupancy_date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    song = forms.ChoiceField(
        label='Dein Saunasong!',
        choices=SONG_CHOICES,
    )

    class Meta:
        model = Occupancy
        exclude = ['user', 'start', 'end']
        fields = ['occupancy_date', 'start_time', 'end_time', 'song', 'notes']
        widgets = {
            'occupancy_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': UltraTimeInput(),
            'end_time': UltraTimeInput()
        }

    def __init__(self, *args, **kwargs):
        super(OccupancyForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs and kwargs['instance'] and hasattr(kwargs['instance'], 'id'):
            self.fields['occupancy_date'].initial = kwargs['instance'].start.date()
            self.fields['start_time'].initial = kwargs['instance'].start.time()
            if kwargs['instance'].end:
                self.fields['end_time'].initial = kwargs['instance'].end.time()
            self.fields['occupancy_date'].widget.attrs['readonly'] = True
            self.fields['start_time'].widget.attrs['readonly'] = True
            self.fields['end_time'].widget.attrs['readonly'] = True
            self.fields['song'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        occupancy_date = cleaned_data.get('occupancy_date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        now = datetime.datetime.now()
        specific_day_occupancies = Occupancy.objects.filter(
            start__year=occupancy_date.year,
            start__month=occupancy_date.month,
            start__day=occupancy_date.day
        )

        if start_time:
            if now.day > occupancy_date.day:
                raise forms.ValidationError(
                    'Du kannst doch nicht in der Vergangenheit saunieren, Dummkopf :)'
                )
            for occupancy in specific_day_occupancies:
                occupancy_start_time = datetime.time(
                    hour=occupancy.start.hour,
                    minute=occupancy.start.minute
                )
                occupancy_end_time = datetime.time(
                    hour=occupancy.end.hour,
                    minute=occupancy.end.minute
                )
                if is_time_in_time_period(occupancy_start_time, occupancy_end_time, start_time):
                    raise forms.ValidationError(
                        'Es wird bereits sauniert, wenn du starten möchtest, schade :('
                    )

        if start_time and end_time:
            if end_time < start_time:
                raise forms.ValidationError(
                    'Du kannst das saunieren nicht beenden bevor du gestartet hast'
                )

    def save(self, commit=True):
        model = super(OccupancyForm, self).save(commit=False)
        model.start = datetime.datetime.combine(self.cleaned_data['occupancy_date'], self.cleaned_data['start_time'])
        model.end = datetime.datetime.combine(self.cleaned_data['occupancy_date'], self.cleaned_data['end_time'])

        if commit:
            model.save()

        return model
