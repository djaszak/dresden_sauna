# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from .forms import OccupancyForm
from .models import Occupancy


def index(request):
    occupancies = Occupancy.objects.all()[:5]

    return render(request, 'index.html', {'occupancies': occupancies})


def create_occupancy(request):
    if request.method == 'POST':
        form = OccupancyForm(request.POST)
        if form.is_valid():
            occupancy = form.save()
            occupancy.user.add(request.user)
            occupancy.save()
            return redirect(index)

    else:
        form = OccupancyForm()

    return render(request, 'create_occupancy.html', {'form': form})


def change_occupancy(request, occupancy_id):
    occupancy = Occupancy.objects.get(pk=occupancy_id)
    if request.method == 'POST':
        form = OccupancyForm(request.POST, instance=occupancy)
        if form.is_valid():
            return redirect(change_occupancy(request, occupancy_id))
    else:
        form = OccupancyForm(instance=occupancy)

    return render(request, 'change_occupancy.html', {'form': form, 'occupancy': occupancy})
