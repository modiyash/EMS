# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.


class Client(models.Model):
    client_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    client_name = models.CharField(max_length=30, null=True)
    client_contract_number = models.CharField(max_length=30, null=True)
    client_pcontact_name = models.CharField(max_length=30, null=True)
    client_pcontact_phone = models.CharField(max_length=13, null=True)
    client_scontact_name = models.CharField(max_length=30, null=True)
    client_scontact_phone = models.CharField(max_length=13, null=True)

    class Meta:
        permissions = (
            ('can_add_client', 'Add new Client'),
            ('can_edit_client', 'Edit Client'),
        )

    def __str__(self):
        return self.client_name + " (" + self.client_id + ")"


class Employee(models.Model):
    employee_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    employee_name = models.CharField(max_length=30, null=True)
    employee_email = models.EmailField(null=True)
    employee_phone = models.CharField(max_length=13, null=True)
    employee_designation = models.CharField(max_length=15, null=True)

    class Meta:
        permissions = (
            ('can_add_employee', 'Add new Employee'),
            ('can_edit_employee', 'Edit Employee'),
        )

    def __str__(self):
        return self.employee_name + " (" + self.employee_id + ")"


class Project(models.Model):
    project_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    project_name = models.CharField(max_length=30, null=True)
    project_purchase_order = models.CharField(max_length=30, null=True)
    project_wbs = models.CharField(max_length=30, null=True)
    project_manager = models.ForeignKey(Employee)
    client_id = models.ForeignKey(Client)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_active = models.NullBooleanField()

    class Meta:
        permissions = (
            ('can_add_project', 'Add new Project'),
            ('can_edit_project', 'Edit Project'),
        )

    def __str__(self):
        return self.project_name + " (" + self.project_id + ")"


class Timesheet(models.Model):
    timesheet_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    timesheet_date = models.DateField(null=True)
    timesheet_week = models.IntegerField(null=True)
    timesheet_dow = models.IntegerField(null=True)
    timesheet_hours = models.CharField(max_length=2, null=True)
    project_id = models.ForeignKey(Project)
    employee_id = models.ForeignKey(Employee)

    class Meta:
        permissions = (
            ('can_add_timesheet', 'Add new Timesheet Entry'),
            ('can_edit_timesheet', 'Edit Timesheet Entry'),
        ),
        unique_together = ("timesheet_date", "project_id", "employee_id")
