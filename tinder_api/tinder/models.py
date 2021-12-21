from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Members(models.Model):
  GENDER_CHOICES = (
    ('M','man'),
    ('F','woman')
  )
  JOB_CHOICES = (
    ('engineering', 'engineering'),
    ('sales', 'sales'),
    ('HR', 'HR'),
    ('marketing', 'marketing')
  )
  gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
  username = CharField(max_length=100)
  age = models.IntegerField()
  introduction = models.CharField(max_length=100)
  job = models.CharField(max_length=20, choices=JOB_CHOICES)

  def __str__(self):
    return self.username