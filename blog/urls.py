from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.bloghome,name='bloghome'),
    #path('ds', views.dshome,name='dshome'),
    #path('<str:slug>', views.blogpost, name='blogpost'),
]