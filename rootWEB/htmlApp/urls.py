from django.contrib import admin
from django.urls import path, include
from htmlApp import views

# http://127.0.0.1:8000/html/xxxx
urlpatterns = [
     # http://127.0.0.1:8000/html/index
    path('index/', views.index),
    # http://127.0.0.1:8000/html/basic_tag
    path('basic_tag/', views.tag),
    # http://127.0.0.1:8000/html/form_tag
    path('form_tag/' , views.form),
    # http://127.0.0.1:8000/html/login
    path('login/'    , views.login)
]