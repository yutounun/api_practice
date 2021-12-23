from django.http import response
from django.shortcuts import render
from rest_framework import views, status
import django_filters
from rest_framework.response import Response
from rest_framework import viewsets, filters

from .models import Members
from .serializer import MemberSerializer

# 全てのHTTPメソッドに対応
# 一番シンプルで早く、個人開発向のModelViewSetで実装してみる
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer