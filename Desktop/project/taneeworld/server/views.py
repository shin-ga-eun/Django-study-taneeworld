from django.shortcuts import render

from .serializers import MemberSerializer, BoardSerializer, CommentSerializer
from .models import Member, Board, Comment
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# from rest_framework.decorators import api_view

# Create your views here.
# DRF 사용법 3.views.py 작성

#클래스 기반 뷰

'''
class board_list(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self,request, format=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class board_detail(APIView):
    """
    코드 조각 조회, 업데이트, 삭제
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    def get_object(self,pk):
        try:
            boards = Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        boards = self.get_object(pk)
        serializer = BoardSerializer(boards)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        boards = self.get(pk)
        serializer = BoardSerializer(boards, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        boards = self.get_object(pk)
        boards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class member_list(APIView):

    def get(self,request,format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)


class member_detail(APIView):
    """
    멤버 회, 업데이트, 삭제
    """
    def get_object(self,pk):
        try:
            members = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        members = self.get_object(pk)
        serializer = MemberSerializer(members)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        members = self.get(pk)
        serializer = MemberSerializer(members, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        members = self.get_object(pk)
        members.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
'''
제네릭 클래스 기반 뷰 사용하기
'''

class board_list(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.member)


class board_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class member_list(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class member_detail(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
