from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email= models.CharField(max_length=15)