# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-06 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0004_auto_20180706_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'permissions': (('can_add_client', 'Add new Client'), ('can_edit_client', 'Edit Client'))},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_add_employee', 'Add new Employee'), ('can_edit_employee', 'Edit Employee'))},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('can_add_project', 'Add new Project'), ('can_edit_project', 'Edit Project'))},
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={'permissions': (('can_add_timesheet', 'Add new Timesheet Entry'), ('can_edit_timesheet', 'Edit Timesheet Entry'))},
        ),
    ]
