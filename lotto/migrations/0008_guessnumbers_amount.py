# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0007_auto_20171112_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='guessnumbers',
            name='amount',
            field=models.CharField(default='1000', max_length=24),
        ),
    ]
