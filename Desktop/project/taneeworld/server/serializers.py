from rest_framework import serializers
from .models import Member, Board, Comment

# DRF 사용법 2.serializer 작성 -> 데이터직렬


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member # 모델 설정
        fields = ('mid','id','pw','mname','isFamily') # 필드 설정


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board # 모델 설정
        fields = ('bid','title','context','created_time','published_time','author') # 필드 설정

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment # 모델 설정
        fields = ('cid','mid','mname','content','created_time','published_time','board') # 필드 설정





