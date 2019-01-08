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

        if start_time:
            if now.day > occupancy_date.day:
                raise forms.ValidationError(
                    'Du kannst doch nicht in der Vergangenheit saunieren, Dummkopf :)'
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
