# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-05 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0002_employee_employee_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_add', 'Add new Employee'),)},
        ),
    ]