from django.http import response
from django.shortcuts import render
from .models import *
from rest_framework import views, status
import django_filters
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

    # getでpk有りの詳細情報を取得する際は下記実行される
    # 下記実行の場合はurlにメソッド名を追加
    @action(methods=['get'], detail=True)
    def attach_san_to_name(self, request, pk=None):
        # Memberの指定したidのレコードを取得
        member = self.get_object()
        # memberの名前+さんをrespond
        return Response('{member.username}さん'.format(member=member))

class JobViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer