from django.db import models
from django.utils import timezone
from django.db import models

# Create your models here.
# DRF 사용법 1.모델작성, admin.py에도 추가.

#멤버
class Member(models.Model):
    mid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=15) #아이디
    pw = models.CharField(max_length=15) #비밀번호
    mname = models.CharField(max_length=30) #이름
    isFamily = models.BooleanField(default=False) #(True=가족, False=팬)

    def __str__(self):
        return self.id


#게시판
class Board(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30) #제목
    context = models.TextField() #게시글
    created_time = models.DateTimeField(default=timezone.now) #작성시간
    published_time = models.DateTimeField(blank=True, null=True) #작성시간
    author = models.ForeignKey(Member, on_delete=models.CASCADE) # Member 테이블 FK /작성
    #댓글 리스트


    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#댓글
class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    mid = models.CharField(max_length=15) #작성자 아이디
    mname = models.CharField(max_length=30) #작성자 이름
    created_time = models.DateTimeField(default=timezone.now)  # 작성시간
    published_time = models.DateTimeField(blank=True, null=True)  # 작성시간
    content = models.TextField() #댓글내용
    board = models.ForeignKey(Board, on_delete=models.CASCADE) # Board 테이블 FK /작성

    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def __str__(self):
        return self.content