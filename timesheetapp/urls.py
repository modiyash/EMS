from django.conf.urls import url
from timesheetapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^home', views.homepage),
    url(r'^employee/$', views.add_employee),
    url(r'^project/$', views.add_project),
    url(r'^client/$', views.add_client),
    url(r'^addtimesheet/$', views.add_timesheet),
    url(r'^record_added/$', views.record_added),
    url(r'^record_updated/$', views.record_updated),
    url(r'^login/$', views.login_user),
    url(r'^logout/$', views.login_user),
    ]