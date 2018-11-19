# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

from .models import Occupancy
from .forms import OccupancyForm


def index(request):
    context = request.context

    return HttpResponse("Hello, world. You're at the polls index.")


def create_occupancy(request):
    if request.method == 'POST':
        form = OccupancyForm(request.POST)
        if form.is_valid():
            render(request, 'create_occupancy.html', {'form': form})

    else:
        form = OccupancyForm()

    return render(request, 'create_occupancy.html', {'form': form})