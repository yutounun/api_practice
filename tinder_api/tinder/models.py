import uuid

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
  # idは外部から読まれないようにuuidかつ編集不可に設定
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='性別')
  username = CharField(max_length=100, unique=True, verbose_name='名前')
  age = models.IntegerField(verbose_name='年齢')
  introduction = models.CharField(max_length=100, null=True, blank=True, verbose_name='自己紹介文')
  job = models.CharField(max_length=20, choices=JOB_CHOICES, verbose_name='職業')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')

  def __str__(self):
    return self.username