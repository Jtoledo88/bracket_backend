from django.db import models


# Create your models here.
class Service(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  def __str__(self):
    return self.title

class Event(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  author = models.CharField(max_length=50)
  day = models.CharField(max_length=250)
  timing = models.CharField(max_length=50)
  def __str__(self):
    return self.title
