# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-03 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_email',
            field=models.EmailField(default='support@test.com', max_length=254),
            preserve_default=False,
        ),
    ]
