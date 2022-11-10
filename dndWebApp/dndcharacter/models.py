from django.db import models

# Create your models here.

class Characters(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length = 50)
    classx = models.CharField(max_length = 50)
    race = models.CharField(max_length = 50)

class Observations(models.Model):
    time = models.DateTimeField()
    temp = models.FloatField()
    sky = models.CharField(max_length = 100)