# Generated by Django 3.1.2 on 2021-12-25 05:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=20, verbose_name='職業名')),
                ('average_salary', models.IntegerField(verbose_name='平均収入')),
                ('paid_holiday_count', models.IntegerField(verbose_name='有給数')),
                ('is_holiday_on_weekend', models.BooleanField(verbose_name='土日休みか')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'man'), ('F', 'woman')], max_length=10, verbose_name='性別')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='名前')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('introduction', models.CharField(blank=True, max_length=100, null=True, verbose_name='自己紹介文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tinder.jobs')),
            ],
        ),
    ]
