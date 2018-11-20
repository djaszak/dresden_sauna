from django import forms
from django.utils import timezone
from django.forms import ModelForm
from .models import Occupancy


class OccupancyForm(ModelForm):
    class Meta:
        model = Occupancy
        exclude = ['user', ]

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')

        if start:
            if timezone.now() > start:
                raise forms.ValidationError(
                    'Du kannst doch nicht in der Vergangenheit saunieren, Dummkopf :)'
                )

        if start and end:
            if end < start:
                raise forms.ValidationError(
                    'Du kannst das saunieren nicht beenden bevor du gestartet hast'
                )
