"""
Project URL configuration for tutor_connect_project.

This file defines the main URL routes for the project. It connects top-level
URLs, such as the homepage and admin area, and includes the URL files from
each Django app so their routes stay organised separately.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin dashboard.
    path("admin/", admin.site.urls),

    # Public homepage.
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

    # Account-related routes, including custom account views.
    path("accounts/", include("accounts.urls")),

    # Built-in Django authentication routes, such as login and logout.
    path("accounts/", include("django.contrib.auth.urls")),

    # App-specific routes.
    path("tutors/", include("tutors.urls")),
    path("bookings/", include("bookings.urls")),
    path("checkout/", include("checkout.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
