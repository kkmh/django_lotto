# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0010_auto_20171113_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nums',
            name='count',
            field=models.IntegerField(),
        ),
    ]