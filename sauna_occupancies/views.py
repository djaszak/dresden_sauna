# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import calendar
import csv
import datetime
import os

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import OccupancyForm
from .models import Occupancy


@login_required(login_url='/sauna_occupancies/login/')
def index(request):
    now = datetime.datetime.now()
    days_of_month = []
    monthrange = calendar.monthrange(now.year, now.month)
    for x in range(monthrange[0]):
        days_of_month.append(('', False))
    for y in range(monthrange[1]):
        if Occupancy.objects.filter(start__year=now.year, start__month=now.month, start__day=y+1).exists():
            days_of_month.append((y + 1, True))
        else:
            days_of_month.append((y + 1, False))
    return render(request, 'index.html', {'days_of_month': days_of_month,
                                          'year': now.year,
                                          'month': calendar.month_name[now.month],
                                          'month_number': now.month})


@login_required(login_url='/sauna_occupancies/login/')
def create_occupancy(request):
    if request.method == 'POST':
        form = OccupancyForm(request.POST)
        if form.is_valid():
            occupancy = form.save()
            occupancy.user.add(request.user)
            occupancy.save()

            # Necassary to get the actual path to our CSV File
            workpath = os.path.dirname(os.path.abspath(__file__))
            ccron = os.path.join(workpath, 'ccron.csv')

            # Mechanism to get latest cronjobID, if there is none yet
            # we get IndexError and generate the least possible ID
            with open(ccron, newline='') as CSVFile:
                reader = list(csv.reader(CSVFile))
                try:
                    # We have to get the last row, the ID is the 9th cell and then we need the numeral ID
                    # without CJ at the beginning
                    numeral_id = int(reader[-1][8][2:])
                    # Now we increment the ID and generate our new cronjobID
                    numeral_id += 1
                    cronjob_id = 'CJ' + str(numeral_id)
                except IndexError:
                    cronjob_id = 'CJ0'

            # Now we will append a new row to the cronjob.csv
            with open(ccron, 'a') as csvFile:
                writer = csv.writer(csvFile)
                # [sec],[min],[hour],[day],*,[month],[year],1,[ID],[comment],0,24,1,*
                minute = occupancy.start.strftime('%M')
                hour = occupancy.start.strftime('%H')
                day = occupancy.start.strftime('%d')
                month = occupancy.start.strftime('%m')
                year = occupancy.start.strftime('%Y')
                comment = occupancy.user.all()[0].__str__()
                writer.writerow([
                    '00',
                    minute,
                    hour,
                    day,
                    '*',
                    month,
                    year,
                    '1',
                    cronjob_id,
                    comment,
                    '0',
                    '24',
                    '1',
                    '*'
                ])
            return redirect(index)
    else:
        form = OccupancyForm()
        for key in request.GET:
            try:
                form.fields[key].initial = request.GET[key]
            except KeyError:
                pass

    return render(request, 'create_occupancy.html', {'form': form})


@login_required(login_url='/sauna_occupancies/login/')
def change_occupancy(request, occupancy_id):
    occupancy = Occupancy.objects.get(pk=occupancy_id)
    if request.method == 'POST':
        form = OccupancyForm(request.POST, instance=occupancy)
        if form.is_valid():
            return render(request, 'change_occupancy.html', {'form': form, 'occupancy': occupancy})
    else:
        form = OccupancyForm(instance=occupancy)

    return render(request, 'change_occupancy.html', {'form': form, 'occupancy': occupancy})


@login_required(login_url='/sauna_occupancies/login/')
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


@login_required(login_url='/sauna_occupancies/login/')
def occupancy_list(request, year, month, day):
    occupancies = Occupancy.objects.filter(start__year=year, start__month=month, start__day=day)
    return render(request, 'occupancy_list.html', {'occupancies': occupancies})

