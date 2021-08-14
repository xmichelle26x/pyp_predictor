from django.db import models
from django.forms.widgets import DateTimeInput

# Create your models here.
class Vehicle(models.Model):
  plate = models.CharField(max_length=7, primary_key=True)
  day = models.DateField()
  # time = models.TimeField()

# class Vehicle(models.Model):
#   plate = models.CharField(max_length=7, primary_key=True)
#   cons_date = models.DateTimeInput(auto_now = False, blank = True) 
