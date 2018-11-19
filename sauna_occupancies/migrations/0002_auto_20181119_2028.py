# Generated by Django 2.1.3 on 2018-11-19 20:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sauna_occupancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupancy',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='occupancy',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 19, 20, 28, 12, 456030)),
        ),
        migrations.AddField(
            model_name='occupancy',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]