# article/admin.py

from django.contrib import admin

from .models import Article

# 注册ArticlePost到admin中
admin.site.register(Article)