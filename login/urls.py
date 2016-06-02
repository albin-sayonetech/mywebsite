from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views
app_name='home'

urlpatterns = [


    url(r'^$', views.login, name='login'),


]