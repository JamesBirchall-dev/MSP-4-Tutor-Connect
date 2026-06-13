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
    path("create/", views.tutor_create, name="tutor_create"),
    path("<int:pk>/edit/", views.tutor_update, name="tutor_update"),
    path("<int:pk>/delete/", views.tutor_delete, name="tutor_delete"),
]
