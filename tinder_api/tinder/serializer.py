from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Members, Jobs

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        # 対象のモデルを指定
        model = Jobs
        # 対象のフィールドを指定
        # created_atは対象外
        fields = ('id', 'average_salary', 'job_name','is_holiday_on_weekend','paid_holiday_count')

class MemberSerializer(serializers.ModelSerializer):
    job = JobSerializer()

    class Meta:
        # 対象のモデルを指定
        model = Members
        # 対象のフィールドを指定
        # created_atは対象外
        fields = ('id', 'gender', 'username','age','introduction', 'job')