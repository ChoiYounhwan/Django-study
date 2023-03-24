from django.urls import path
from cssApp import views

# http:// 127.0.0.1:8000/css
urlpatterns = [
    #http://127.0.0.1:8000/css/main
    path('main/', views.index),
    path('external/', views.external),
    path('selector/', views.selector),
    path('descendant/', views.descendant),
    path('box/', views.box),
    path('layout/', views.layout),
]

