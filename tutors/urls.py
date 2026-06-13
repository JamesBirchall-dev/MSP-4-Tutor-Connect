"""
URL configuration for this app.

This file maps URL paths to the views that handle them. Each route defined
here is usually included in the main project-level urls.py file.
"""
from django.urls import path
from . import views

app_name = 'tutors'

urlpatterns = [
    path('', views.tutor_list, name='tutor_list'),
    path('<int:pk>/', views.tutor_detail, name='tutor_detail'),
]
