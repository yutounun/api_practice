from django.http import response
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import views, status
import django_filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
# @actionを利用するために必要
from rest_framework.decorators import action

from .models import Members
from .serializer import MemberSerializer, JobSerializer

# ログ処理
import logging
from logging import getLogger, StreamHandler, Formatter

# 全てのHTTPメソッドに対応
# 一番シンプルで早く、個人開発向のModelViewSetで実装してみる
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    # このViewSetはログイン済みのaccess_tokenを持つuserしかたたけない
    permission_classes = (IsAuthenticated,)

    # 取得したクエリセットを念のためdjango.logとターミナルに出力
    logger = logging.getLogger('command')
    logger.info(queryset)

    @action(methods=['get'], detail=True)
    def error_handling(self, request, pk=None):
        # getメソッドでIDが存在しないときはNotFoundエラーを発生させる
        # Memberの指定したidのレコードを取得
        try:
            obj = self.get_object()
            # objのログをターミナルとファイルに出力
            logger = logging.getLogger('command')
            logger.info(obj)
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        except:
            raise NotFound

class JobViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer