from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('gamma/', views.gamma, name='man'),


]