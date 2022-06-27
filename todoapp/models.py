from turtle import title
from django.db import models

# Create your models here.

class tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    username = models.TextField(default='Null')
    important = models.BooleanField(default=False)