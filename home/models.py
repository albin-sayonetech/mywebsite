from __future__ import unicode_literals

from django.db import models
from register.models import models

class Event(models.Model):
      date=models.DateField(max_length=100)
      time=models.TimeField(max_length=100)
      title=models.CharField(max_length=50)
      details=models.CharField(max_length=100000)

class Comment(models.Model):
      date = models.DateField(max_length=100)
      time = models.TimeField(max_length=100)
      usercomm=models.CharField(max_length=100000)