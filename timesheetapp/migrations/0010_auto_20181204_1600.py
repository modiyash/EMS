# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-04 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0009_auto_20181204_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_phone',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
    ]
