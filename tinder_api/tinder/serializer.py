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
    class Meta:
        # 対象のモデルを指定
        model = Members
        # 対象のフィールドを指定
        # created_atは対象外
        fields = ('id', 'gender', 'username','age','introduction', 'job')
    
    # POST時はForeignKeyをpkのみ指定し、GET時はネストしたオブジェクトを展開する
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['job'] = JobSerializer(instance.job).data
        return response