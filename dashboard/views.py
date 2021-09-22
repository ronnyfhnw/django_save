from django.shortcuts import render
from django.http import HttpResponse
from . import funs
import datetime as dt
from .forms import DateInput

# Create your views here.
def home(request):
      return HttpResponse(render(request, 'app/home.html'))

def air(request):
      return HttpResponse(render(request, 'app/air.html'))

def oura(request):
      # fetch data from db
      sleep = funs.sleep_score()
      activity = funs.activity_score()
      readiness = funs.readiness_score()

      readiness_data = funs.get_readiness_data()

      # preparing context
      context = {'sleep': sleep[0], 'sleep_diff': sleep[1], 'activity':activity[0], 'activity_diff':activity[1], 'readiness':readiness[0], 'readiness_diff':readiness[1], 'readiness_data':readiness_data}
      return HttpResponse(render(request, 'app/oura.html', context))

def oura_activity(request):
      # setting standart values
      sleep_date = dt.datetime.now().strftime('%Y-%m-%d')
      measurement = 'activity_score'

      if request.method == "POST":
            items = list(request.POST.items())
            for key, value in items:
                  if key == 'sleep_date':
                        sleep_date = request.POST.get('sleep_date')
                  elif key == 'button':
                        measurement = str(value)
            
      data = funs.activity_data_detailed(dt.datetime.strptime(sleep_date, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S'))

      last_7 = funs.get_last_7_activity(measurement)

      context = {'data': data, 'date':sleep_date, 'last_7':last_7, 'measurement': measurement}

      return HttpResponse(render(request, 'app/oura_activity.html', context))

def oura_sleep(request):
      # setting standart values
      sleep_date = dt.datetime.now().strftime('%Y-%m-%d')
      measurement = 'sleep_score'

      if request.method == "POST":
            items = list(request.POST.items())
            for key, value in items:
                  if key == 'sleep_date':
                        sleep_date = request.POST.get('sleep_date')
                  elif key == 'button':
                        measurement = str(value)
            
      data = funs.sleep_data_detailed(dt.datetime.strptime(sleep_date, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S'))

      last_7 = funs.get_last_7_sleep(measurement)

      context = {'data': data, 'date':sleep_date, 'last_7':last_7, 'measurement': measurement}

      return HttpResponse(render(request, 'app/oura_sleep.html', context))

def activities(request):
      return HttpResponse(render(request, 'app/activities.html'))

def todo(request):
      return HttpResponse(render(request, 'app/todo.html'))


