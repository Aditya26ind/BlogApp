from django.contrib import admin
from django.urls import path,include
from .views import homeview

urlpatterns = [
    path('',homeview,name='news'),
]