from django.http import response
from django.shortcuts import render
from .models import *
from rest_framework import views, status
import django_filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import viewsets, filters
# @actionを利用するために必要
from rest_framework.decorators import action

from .models import Members
from .serializer import MemberSerializer, JobSerializer

# 全てのHTTPメソッドに対応
# 一番シンプルで早く、個人開発向のModelViewSetで実装してみる
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    
    # getメソッドでIDが存在しないときはNotFoundエラーを発生させる
    @action(methods=['get'], detail=True)
    def error_handling(self, request, pk=None):
        # Memberの指定したidのレコードを取得
        try:
            obj = self.get_object()
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        except:
            raise NotFound

class JobViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer