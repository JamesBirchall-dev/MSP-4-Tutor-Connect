"""
URL configuration for this app.

This file maps URL paths to the views that handle them. Each route defined
here is usually included in the main project-level urls.py file.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("<int:booking_pk>/", views.checkout, name="checkout"),
    path(
        "<int:booking_pk>/create-session/",
        views.create_checkout_session,
        name="create_checkout_session",
    ),
    path("success/", views.checkout_success, name="checkout_success"),
    path("cancelled/", views.checkout_cancelled, name="checkout_cancelled"),
]
