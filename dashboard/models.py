from django.db import models

# Create your models here.
class sleep(models.Model):
      timestamp = models.CharField(max_length=50)
      sleep_score = models.IntegerField()
      duration = models.IntegerField()
      time_in_bed = models.IntegerField()
      efficency = models.IntegerField()
      restfulness = models.IntegerField()
      rem = models.IntegerField()
      deep = models.IntegerField()
      light = models.IntegerField()
      latency = models.IntegerField()
      heartrate = models.FloatField()

class activity(models.Model):
      timestamp = models.CharField(max_length=50)
      activity_score = models.IntegerField()
      steps = models.IntegerField()
      calories = models.IntegerField()
      score_meet_daily_targets = models.IntegerField()
      score_recovery_time = models.IntegerField()
      score_training_volume = models.IntegerField()

class readiness(models.Model):
      timestamp = models.CharField(max_length=50)
      readiness_score = models.IntegerField()

class air(models.Model):
      timestamp = models.DateTimeField()
      co2 = models.IntegerField()
      temp = models.FloatField()
      hum = models.FloatField()