# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0006_auto_20180711_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timesheet',
            options={'permissions': ((('can_add_timesheet', 'Add new Timesheet Entry'), ('can_edit_timesheet', 'Edit Timesheet Entry')),)},
        ),
        migrations.AlterUniqueTogether(
            name='timesheet',
            unique_together=set([('timesheet_date', 'project_id', 'employee_id')]),
        ),
    ]
