# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Occupancy(models.Model):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(blank=True,
                               null=True)
    user = models.ForeignKey(User,
                             verbose_name='User',
                             on_delete=models.PROTECT,
                             blank=True,
                             null=True)

