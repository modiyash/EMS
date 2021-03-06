# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-06 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0003_auto_20180705_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_pcontact_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_pcontact_phone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_scontact_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_scontact_phone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_designation',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_phone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='is_active',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='timesheet_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='timesheet_hours',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
