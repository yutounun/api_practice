import uuid

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
class Members(models.Model):
    GENDER_CHOICES = (
        ('M','man'),
        ('F','woman')
    )
    # idは外部から読まれないようにuuidかつ編集不可に設定
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='性別')
    username = CharField(max_length=100, unique=True, verbose_name='名前')
    age = models.IntegerField(verbose_name='年齢')
    introduction = models.CharField(max_length=100, null=True, blank=True, verbose_name='自己紹介文')
    job = models.ForeignKey('Jobs', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')

    def __str__(self):
        return self.username

class Jobs(models.Model):
    job_name = models.CharField(max_length=20, verbose_name='職業名')
    average_salary = models.IntegerField(verbose_name='平均収入')
    paid_holiday_count = models.IntegerField(verbose_name='有給数')
    is_holiday_on_weekend = models.BooleanField(verbose_name='土日休みか')
    
    def __str__(self):
        return self.job_name