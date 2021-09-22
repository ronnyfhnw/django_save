from dashboard.models import sleep, activity, readiness
import datetime as dt
import pandas as pd
from django.db import connection

def sleep_score():
      data_available = True
      # setting dates for sql query
      today = (dt.datetime.now() - dt.timedelta(days=0)).date().strftime('%Y-%m-%d %H:%M:%S')
      yesterday = (dt.datetime.now() - dt.timedelta(days=1)).date().strftime('%Y-%m-%d %H:%M:%S')

      # getting data from db
      try:
            sleep_score = [sleep.objects.raw(f"SELECT * FROM dashboard_sleep WHERE timestamp='{today}'")[0].sleep_score, sleep.objects.raw(f"SELECT * FROM dashboard_sleep WHERE timestamp='{yesterday}'")[0].sleep_score]
      except IndexError:
            sleep_score = ['NA', 'NA']
            data_available = False

      # calculating difference to yesterday
      if data_available:
            sleep_score[1] = sleep_score[0] - sleep_score[1]

      return sleep_score

def activity_score():
      data_available = True
      # setting dates for sql query
      today = (dt.datetime.now() - dt.timedelta(days=0)).date().strftime('%Y-%m-%d %H:%M:%S')
      yesterday = (dt.datetime.now() - dt.timedelta(days=1)).date().strftime('%Y-%m-%d %H:%M:%S')

      # getting data form db
      try:
            activity_score = [activity.objects.raw(f"SELECT * FROM dashboard_activity WHERE timestamp='{today}'")[0].activity_score, activity.objects.raw(f"SELECT * FROM dashboard_activity WHERE timestamp='{yesterday}'")[0].activity_score]
      except IndexError:
            activity_score = ['NA', 'NA']
            data_available = False

      # calculating difference to yesterday
      if data_available:
            activity_score[1] = activity_score[0] - activity_score[1]

      return activity_score

def readiness_score():
      data_available = True
      # setting dates for query
      today = (dt.datetime.now() - dt.timedelta(days=1)).date().strftime('%Y-%m-%d %H:%M:%S')
      yesterday = (dt.datetime.now() - dt.timedelta(days=2)).date().strftime('%Y-%m-%d %H:%M:%S')

      # getting data from yesterday
      try:
            readiness_score = [readiness.objects.raw(f"SELECT * FROM dashboard_readiness WHERE timestamp='{today}'")[0].readiness_score, readiness.objects.raw(f"SELECT * FROM dashboard_readiness WHERE timestamp='{yesterday}'")[0].readiness_score]
      except IndexError:
            readiness_score = ['NA', 'NA']
            data_available = False

      # calculating difference to yesterday
      if data_available:
            readiness_score[1] = readiness_score[0] - readiness_score[1]

      return readiness_score

def sleep_data_detailed(date:str):
      data_available = True
      # querying data from db
      df = pd.read_sql_query(f"SELECT * FROM dashboard_sleep WHERE timestamp='{date}'", connection)
      
      # exceptions for not synchronized data
      try:
            df = df.iloc[0,:]
            df = df.drop(index=['id', 'timestamp'])
            data = df.to_dict()
      except IndexError:
            data = {}
            data_available = False

      # data transformations
      if data_available:
            context = []
            for key in list(data.keys()):
                  context.append({'name': key, 'value': data[key]})
            for i in [1, 2, 5, 6, 7]:
                  context[i]['value'] = str(dt.timedelta(seconds=int(context[i]['value'])))[:-3]

      else:
            context = []
      
      return context

def get_last_7_sleep(filter_string:str):
      data_available = True
      df = pd.read_sql_query("SELECT * FROM dashboard_sleep ORDER BY timestamp DESC LIMIT 10", connection)

      df = df.drop(columns=['id'])
      df['timestamp'] = df['timestamp'].apply(lambda x: x.rstrip('00:00:00'))
      df = df[['timestamp', filter_string]]
      df.columns = ['timestamp', 'data']
      data = df.to_dict('records')

      return data

def activity_data_detailed(date:str):
      data_available = True
      # querying data from db
      df = pd.read_sql_query(f"SELECT * FROM dashboard_activity WHERE timestamp='{date}'", connection)
      
      # exceptions for not synchronized data
      try:
            df = df.iloc[0,:]
            df = df.drop(index=['id', 'timestamp'])
            data = df.to_dict()
      except IndexError:
            data = {}
            data_available = False

      print(df)

      # data transformations
      if data_available:
            context = []
            for key in list(data.keys()):
                  context.append({'name': key, 'value': data[key]})
      else:
            context = []
      
      return context

def get_last_7_activity(filter_string:str):
      data_available = True
      df = pd.read_sql_query("SELECT * FROM dashboard_activity ORDER BY timestamp DESC LIMIT 10", connection)

      df = df.drop(columns=['id'])
      df['timestamp'] = df['timestamp'].apply(lambda x: x.rstrip('00:00:00'))
      df = df[['timestamp', filter_string]]
      df.columns = ['timestamp', 'data']
      data = df.to_dict('records')

      return data

def get_readiness_data():
      df = pd.read_sql_query("SELECT * FROM dashboard_readiness", connection)
      df = df.reset_index(drop=True)
      print(df)

      df = df.iloc[:10,:]

      data = df.to_dict('records')

      return data