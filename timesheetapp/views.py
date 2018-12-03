# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import EmployeeForm, TimesheetForm, LoginForm, ProjectForm, ClientForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

from django.http import *
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.template import loader
from timesheetapp.models import Timesheet, Employee, Project, Client
from datetime import date, timedelta
# Create your views here.


@login_required(login_url='/login/')
def homepage(request):
    if request.GET.get('week') == None:
        current_week = int(date.today().isocalendar()[1])
        current_day = date.today().isocalendar()[2]
        monday = date.today() - timedelta(current_day - 1)
        sunday = date.today() + timedelta(7 - current_day)
    else:
        current_week = int(request.GET.get('week'))
        a_current_week = int(date.today().isocalendar()[1])
        diff_week = a_current_week - current_week
        current_day = date.today().isocalendar()[2]
        monday = date.today() - timedelta(current_day - 1 + (7 * diff_week))
        sunday = date.today() + timedelta(7 - current_day - (7 * diff_week))
    if request.user.has_perm('timesheetapp.can_add_employee'):
        template = loader.get_template('index.html')
        emps = Employee.objects.all()
        result = []
        for e in emps:
            row = {}
            row['name'] = e.employee_name
            row['timesheets'] = []
            for proj in Project.objects.all().order_by('id'):
                innerrow = {}
                innerrow['project'] = proj.project_name
                innerrow['hours'] = []
                counter = 0
                weektimesheets = Timesheet.objects.filter(employee_id=e.id, timesheet_week=current_week,
                                                          project_id=proj.id).order_by('timesheet_dow')
                for i in range(1, 8):
                    if counter < len(weektimesheets) and weektimesheets[counter].timesheet_dow == i:
                        innerrow['hours'].append(int(weektimesheets[counter].timesheet_hours))
                        counter = counter + 1
                    else:
                        innerrow['hours'].append(0)
                rowtotal = sum(innerrow['hours'])
                innerrow['hours'].append(rowtotal)
                row['timesheets'].append(innerrow)
            total = {}
            total['project'] = "Total"
            total['hours'] = []
            for i in range(8):
                coltotal = 0
                for proj in row['timesheets']:
                    coltotal += proj['hours'][i]
                total['hours'].append(coltotal)
            row['timesheets'].append(total)
            result.append(row)
    else:
        emppk = Employee.objects.filter(employee_email=str(request.user))[0].id
        result = []
        for proj in Project.objects.all().order_by('id'):
            row = {}
            row['project'] = proj.project_name
            row['hours'] = []
            counter = 0
            weektimesheets = Timesheet.objects.filter(employee_id=emppk, timesheet_week=current_week,
                                                      project_id=proj.id).order_by('timesheet_dow')
            for i in range(1, 8):
                if counter < len(weektimesheets) and weektimesheets[counter].timesheet_dow == i:
                    row['hours'].append(int(weektimesheets[counter].timesheet_hours))
                    counter = counter + 1
                else:
                    row['hours'].append(0)
            rowtotal = sum(row['hours'])
            row['hours'].append(rowtotal)
            result.append(row)
        total = {}
        total['project'] = "Total"
        total['hours'] = []
        for i in range(8):
            coltotal = 0
            for proj in result:
                coltotal += proj['hours'][i]
            total['hours'].append(coltotal)
        result.append(total)
        template = loader.get_template('index2.html')
    context = {
        'current_week': "Week #" + str(current_week),
        'date_range': monday.strftime('%m-%d-%Y') + " to " + sunday.strftime('%m-%d-%Y'),
        'items': result,
        'next': (current_week + 1),
        'prev': (current_week - 1)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            e = Employee(employee_name=form.cleaned_data['employee_name'],
                         employee_email=form.cleaned_data['employee_email'],
                         employee_phone=form.cleaned_data['employee_phone'],
                         employee_designation=form.cleaned_data['employee_designation'])
            e.save()
            user = User.objects.create_user(username=e.employee_email, password='defaultpassword')
            permission = Permission.objects.get(name='Add new Timesheet Entry')
            user.user_permissions.add(permission)
            user.save()
            return HttpResponseRedirect('/record_added/')
    else:
        if request.user.has_perm('timesheetapp.can_add_employee'):
            form = EmployeeForm()
        else:
            return render_to_response('unauthorised.html')

    return render(request, 'add_employee.html', {'form': form})


@login_required(login_url='/login/')
def record_added(request):
    return render(request, 'record_added.html', context=None)


@login_required(login_url='/login/')
def record_updated(request):
    return render(request, 'record_updated.html', context=None)


@login_required(login_url='/login/')
def add_timesheet(request):
    if request.method == 'POST':
        form = TimesheetForm(request.POST)
        if form.is_valid():
            dateitems = str(form.cleaned_data['date']).split("-")
            exists = Timesheet.objects.filter(timesheet_date=form.cleaned_data['date'],
                                              project_id=form.cleaned_data['project_id'],
                                              employee_id=Employee.objects.filter(employee_email=str(request.user))[0])
            if len(exists) > 0:
                t = Timesheet.objects.get(id=exists[0].id)
                t.timesheet_hours = form.cleaned_data['hours']
                t.save()
                return HttpResponseRedirect('/record_updated/')
            else:
                t = Timesheet(timesheet_date=form.cleaned_data['date'],
                              timesheet_week=date(int(dateitems[0]), int(dateitems[1]), int(dateitems[2])).isocalendar()[1],
                              timesheet_dow=date(int(dateitems[0]), int(dateitems[1]), int(dateitems[2])).isocalendar()[2],
                              timesheet_hours=form.cleaned_data['hours'],
                              project_id=form.cleaned_data['project_id'],
                              employee_id=Employee.objects.filter(employee_email=str(request.user))[0])
                t.save()
                return HttpResponseRedirect('/record_added/')
    else:
        if request.user.has_perm('timesheetapp.can_add_timesheet'):
            form = TimesheetForm()
        else:
            return render_to_response('unauthorised.html')

    return render(request, 'add_timesheet.html', {'form': form})

@login_required(login_url='/login/')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            p = Project(project_name=form.cleaned_data['project_name'],
                        client_id=form.cleaned_data['client_id'],
                        project_manager=form.cleaned_data['project_manager'],
                        is_active=True)
            p.save();
            return HttpResponseRedirect('/record_added/')
    else:
        if request.user.has_perm('timesheetapp.can_add_project'):
            form = ProjectForm()
        else:
            return render_to_response('unauthorised.html')

    return render(request, 'add_project.html', {'form': form})

@login_required(login_url='/login/')
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            c = Client(client_name=form.cleaned_data['client_name'],
                       client_contract_number=form.cleaned_data['client_contract_number'],
                       client_pcontact_name=form.cleaned_data['client_pcontact_name'],
                       client_pcontact_phone=form.cleaned_data['client_pcontact_phone'],
                       client_scontact_name=form.cleaned_data['client_scontact_name'],
                       client_scontact_phone=form.cleaned_data['client_scontact_phone'],
                       )
            c.save();
            return HttpResponseRedirect('/record_added/')
    else:
        if request.user.has_perm('timesheetapp.can_add_client'):
            form = ClientForm()
        else:
            return render_to_response('unauthorised.html')

    return render(request, 'add_client.html', {'form': form})


def login_user(request):
    logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
        else:
            raise KeyError
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})