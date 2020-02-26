from django.contrib import admin
from .models import Member, Board, Comment
# Register your models here.

admin.site.register(Member)
admin.site.register(Board)
admin.site.register(Comment)

