from django.http import response
from django.shortcuts import render
from rest_framework import views, status
import django_filters
from rest_framework.response import Response
from rest_framework import viewsets, filters

from .models import Members
from .serializer import MemberSerializer, SpecificMemberRequestSerializer, SpecificMemberResponseSerializer

# メンバーのデータ一覧取得
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

# 指定したメンバーデータを取得
class SpecificMemberAPIView(views.APIView):
    def get(self, request, member_id):
      # 後にtokenなどが入る可能性もあるため配列にしておく
      request_data = request.data
      request_data['member_id'] = member_id
      request_serializer = SpecificMemberRequestSerializer(data=request_data)
      # requestのバリデーションを実行
      if request_serializer.is_valid():
        # SpecificMemberRequestSerializer内createメソッド実行
        response_data = request_serializer.save()
        # requestだけではなくresponseもバリデーションを行う
        response_serializer = SpecificMemberResponseSerializer(response_data)
        return Response(
          # レスポンスされるデータはserializerのdataに格納される
          response_serializer.data
        )

