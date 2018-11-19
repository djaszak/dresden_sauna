from django import forms
from django.forms import ModelForm
from django.forms.widgets import SplitDateTimeWidget
from .models import Occupancy


class OccupancyForm(ModelForm):
    class Meta:
        model = Occupancy
        exclude = ['user', ]
        # widgets = {
        #     'start': SplitDateTimeWidget(date_attrs={'type': 'date'},
        #                                  time_attrs={'type': 'time'}, ),
        #     'end': SplitDateTimeWidget,
        # }
