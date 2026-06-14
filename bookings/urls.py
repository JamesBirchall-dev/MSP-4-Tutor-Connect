"""
URL configuration for this app.

This file maps URL paths to the views that handle them. Each route defined
here is usually included in the main project-level urls.py file.
"""

from django.urls import path
from . import views

app_name = "bookings"

urlpatterns = [
    path("", views.booking_list, name="booking_list"),
    path(
        "create/<int:lesson_pk>/",
        views.booking_create,
        name="booking_create",
    ),
    path("<int:pk>/edit/", views.booking_update, name="booking_update"),
    path("<int:pk>/delete/", views.booking_delete, name="booking_delete"),
]
