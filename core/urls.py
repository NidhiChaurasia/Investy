from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.input,name="input"),
    path('results/', views.output,name="output"),
]
