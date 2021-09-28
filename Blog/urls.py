from django.contrib import admin
from django.urls import path,include
from .views import blog, blogdelete

urlpatterns = [
    path('',blog,name='blog'),
    path('<int:pk>/',blogdelete,name='blogdelete'),
]