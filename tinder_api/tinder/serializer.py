from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Members


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        # 対象のモデルを指定
        model = Members
        # 対象のフィールドを指定
        fields = ['__all__']

# requestのバリデーションを行う 
class SpecificMemberRequestSerializer(serializers.Serializer):
    member_id = serializers.IntegerField()

    def create(self, validated_data):
        member_id = validated_data['member_id']
        # マッチするデータがない場合には404エラーを表示
        response_data = get_object_or_404(Members, id=member_id)
        return response_data

# responseの際にもバリデーションを行う
class SpecificMemberResponseSerializer(serializers.Serializer):
    gender = serializers.CharField()
    username = serializers.CharField()
    age = serializers.IntegerField()
    introduction = serializers.CharField()
    job = serializers.CharField()