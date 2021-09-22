from django.contrib import admin
from django.urls import path
from . import views
from dash_apps.finished_apps import input, readiness_plot, date_picker


urlpatterns = [
      path('', views.home, name='home'),
      path('air/', views.air, name='air'),
      path('oura/', views.oura, name='oura'),
      path('oura/activity/', views.oura_activity, name='oura_activity'),
      path('oura/sleep', views.oura_sleep, name='oura_sleep'),
      path('activities/', views.activities, name='activities'),
      path('todo/', views.todo, name='todo')
]