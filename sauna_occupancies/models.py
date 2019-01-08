# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Occupancy(models.Model):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(blank=True,
                               null=True)
    user = models.ManyToManyField(User,
                                  verbose_name='User',
                                  blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return 'Diese Belegung startet um {} Uhr und endet um {} Uhr.'.format(
            self.start.strftime('%H:%M'),
            self.end.strftime('%H:%M'))
