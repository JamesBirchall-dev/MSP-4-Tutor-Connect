"""
URL configuration for this app.

This file maps URL paths to the views that handle them. Each route defined
here is usually included in the main project-level urls.py file.
"""

from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path(
        "booking/<int:booking_pk>/",
        views.checkout_review,
        name="checkout_review",
         ),
    path(
        "booking/<int:booking_pk>/create-session/",
        views.create_checkout_session,
        name="create_checkout_session",
    ),
    path(
        "success/",
        views.checkout_success,
        name="checkout_success"),
    path(
        "cancelled/",
        views.checkout_cancelled,
        name="checkout_cancelled"),
    path(
        "webhook/",
        views.stripe_webhook,
        name="stripe_webhook"),
]
