# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import OccupancyForm
from .models import Occupancy


@login_required
def index(request):
    occupancies = Occupancy.objects.all()[:5]

    return render(request, 'index.html', {'occupancies': occupancies})


@login_required
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


@login_required
def change_occupancy(request, occupancy_id):
    occupancy = Occupancy.objects.get(pk=occupancy_id)
    if request.method == 'POST':
        form = OccupancyForm(request.POST, instance=occupancy)
        if form.is_valid():
            return render(request, 'change_occupancy.html', {'form': form, 'occupancy': occupancy})
    else:
        form = OccupancyForm(instance=occupancy)

    return render(request, 'change_occupancy.html', {'form': form, 'occupancy': occupancy})


@login_required
def add_user_to_occupancy(request, occupancy_id):
    occupancy = Occupancy.objects.get(pk=occupancy_id)
    user = request.user
    if occupancy.user.filter(id=user.id).exists():
        messages.error(request, 'Du bist schon in dieser Belegung, reicht dann auch!')
        return redirect(change_occupancy, occupancy_id=occupancy.id)
    else:
        occupancy.user.add(user)
        occupancy.save()
        messages.success(request, 'Nice, du saunierst dann auch mit')
        return redirect(change_occupancy, occupancy_id=occupancy.id)

