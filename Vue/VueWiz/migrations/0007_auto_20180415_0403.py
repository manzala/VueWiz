# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-15 04:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VueWiz', '0006_auto_20180415_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
