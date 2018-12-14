from django import forms
from django.contrib.admin import widgets
from django.utils import timezone
from django.forms.widgets import TimeInput

from .models import Occupancy

class UltraDateInput(forms.DateInput):
    input_type = 'date'
    

class UltraTimeInput(forms.TimeInput):
    input_type = 'time'

class OccupancyForm(forms.ModelForm):
    occupancy_date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()

    class Meta:
        model = Occupancy
        exclude = ['user', 'start', 'end']
        fields = ['occupancy_date', 'start_time', 'end_time', 'notes']
        widgets = {
            'occupancy_date': UltraDateInput(),
            'start_time': UltraTimeInput(),
            'end_time': UltraTimeInput()
        }

    def __init__(self, *args, **kwargs):
        super(OccupancyForm, self).__init__(*args, **kwargs)

        # if kwargs['instance']:
        #     self.fields['occupancy_date'].initial = kwargs['instance'].start.date()
        #     self.fields['start_time'].initial = kwargs['instance'].start.time()
        # if kwargs['instance'].end:
        #     self.fields['end_time'].initial = kwargs['instance'].end.time()

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start')
        end_time = cleaned_data.get('end')

        if start_time:
            if timezone.now() > start_time:
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
        model.start = datetime.combine(self.cleaned_data['occupancy_date'], self.cleaned_data['start_time'])
        model.end = datetime.combine(self.cleaned_data['occupancy_date'], self.cleaned_data['end_time'])

        if commit:
            model.save()

        return model
