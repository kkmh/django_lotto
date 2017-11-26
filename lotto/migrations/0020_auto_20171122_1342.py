# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0019_auto_20171122_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decidednumbers',
            name='shotDate',
            field=models.DateField(),
        ),
        migrations.AddIndex(
            model_name='decidednumbers',
            index=models.Index(fields=['shotDate'], name='lotto_decid_shotDat_0b0549_idx'),
        ),
    ]