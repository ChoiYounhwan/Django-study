from django.contrib import admin
from django.urls import path, include
from htmlApp import views

# http://127.0.0.1:8000/html/xxxx
urlpatterns = [
     # http://127.0.0.1:8000/html/xxxx
    path('index/', views.index),
    path('basic_tag/', views.tag)
]