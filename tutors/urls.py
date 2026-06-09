"""
URL configuration for this app.

This file maps URL paths to the views that handle them. Each route defined
here is usually included in the main project-level urls.py file.
"""
from django.urls import include, path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path("", views.tutor_list, name="tutor_list"),
    path("<int:pk>/", views.tutor_detail, name="tutor_detail"),
    path("create/", views.tutor_create, name="tutor_create"),
    path("<int:pk>/edit/", views.tutor_update, name="tutor_update"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]


def tutor_list(request):
    """Display a temporary tutor list placeholder view."""
    return HttpResponse("Tutor list placeholder")


def tutor_detail(request, pk):
    """Display a temporary tutor detail placeholder view."""
    return HttpResponse(f"Tutor detail placeholder for tutor {pk}")


def tutor_create(request):
    """Display a temporary tutor create placeholder view."""
    return HttpResponse("Tutor create placeholder")


def tutor_update(request, pk):
    """Display a temporary tutor update placeholder view."""
    return HttpResponse(f"Tutor update placeholder for tutor {pk}")
