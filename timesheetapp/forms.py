from django import forms
from .models import Project, Client, Employee

class EmployeeForm(forms.Form):
    employee_name = forms.CharField(label='Name', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    employee_email = forms.EmailField(label='Email',
                                      widget=forms.EmailInput(attrs={'class': 'form-control'}))
    employee_phone = forms.CharField(label='Contact No.',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    employee_designation = forms.CharField(label='Designation',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))


class TimesheetForm(forms.Form):
    project_id = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label='Select Project',
                                        label="Project ID", widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    hours = forms.DecimalField(label='Hours', widget=forms.NumberInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Username',
                                                                       'required':'',
                                                                       'autofocus':''}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Password',
                                                                           'required':''}))

class ProjectForm(forms.Form):
    project_name = forms.CharField(label='Name', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_id = forms.ModelChoiceField(queryset=Client.objects.all(), empty_label='Select Client',
                                        label="Client ID", widget=forms.Select(attrs={'class': 'form-control'}))
    project_manager = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label='Appoint Manager',
                                        label="Project Manager", widget=forms.Select(attrs={'class': 'form-control'}))

class ClientForm(forms.Form):
    client_name = forms.CharField(label='Name', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_contract_number = forms.CharField(label='Contract Number', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_pcontact_name = forms.CharField(label='Primary Contact Name', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_pcontact_phone = forms.CharField(label='Primary Contact Phone', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_scontact_name = forms.CharField(label='Secondary Contact Name', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_scontact_phone = forms.CharField(label='Secondary Contact Phone', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
