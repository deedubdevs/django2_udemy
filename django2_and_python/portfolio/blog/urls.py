from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views
from portfolio import settings

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail')
]
