# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-15 03:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VueWiz', '0004_auto_20180414_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadmodel',
            name='user',
            field=models.OneToOneField(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploadmodel',
            name='pdfFile',
            field=models.FileField(blank=True, db_column=b'pdffile', help_text=b'Load a pdf.', null=True, upload_to=b''),
        ),
    ]
