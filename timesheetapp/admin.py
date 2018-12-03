# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

import models as m

class Client(admin.ModelAdmin):
    fields = ("client_id", "client_name", "client_pcontact_name", "client_pcontact_phone", "client_scontact_name",
              "client_scontact_phone")
    list_display = ("client_id", "client_name", "client_pcontact_name", "client_pcontact_phone", "client_scontact_name",
                    "client_scontact_phone")


class Employee(admin.ModelAdmin):
    fields = ("employee_id", "employee_name", "employee_email", "employee_phone", "employee_designation")
    list_display = ("employee_id", "employee_name", "employee_email", "employee_phone", "employee_designation")


class Project(admin.ModelAdmin):
    fields = ("project_id", "project_name", "project_manager", "client_id", "start_date", "end_date", "is_active")
    list_display = ("project_id", "project_name", "project_manager", "client_id", "start_date", "end_date", "is_active")


class Timesheet(admin.ModelAdmin):
    fields = ("timesheet_id", "timesheet_date", "timesheet_week", "timesheet_dow", "timesheet_hours", "project_id", "employee_id")
    list_display = ("timesheet_id", "timesheet_date", "timesheet_week", "timesheet_dow", "timesheet_hours", "project_id", "employee_id")

# Register your models here.


admin.site.register(m.Employee, Employee)
admin.site.register(m.Client, Client)
admin.site.register(m.Project, Project)
admin.site.register(m.Timesheet, Timesheet)
