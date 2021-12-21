# coding: utf-8

from rest_framework import serializers

from .models import Members


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'gender', 'username','age','introduction', 'job')