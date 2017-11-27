# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0031_forminput'),
    ]

    operations = [
        migrations.AddField(
            model_name='forminput',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
