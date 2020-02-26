from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MemberSerializer, BoardSerializer, CommentSerializer
from .models import Member, Board, Comment

# Create your views here.
# DRF 사용법 3.views.py 작성 -> viewsets를 통해 CRUD 적용.


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer