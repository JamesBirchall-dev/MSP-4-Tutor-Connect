from django.contrib import admin
from tutors.models import LessonType, TutorProfile


@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TutorProfile model.

    Provides a quick visibility of tutor status and profile info.
    Supports filtering and search for efficient admin.
    """

    # Key profile info
    list_display = ("display_name", "user", "is_active", "created_at")

    # common filters used to manage active tutors
    list_filter = ("is_active", "location", "created_at")

    # enables admin users to search by display name and email
    search_fields = (
        "display_name",
        "user__username",
        "user__email",
        "bio",
        "experience",
        "location",
    )

    # Display profiles alphabetically by display name
    ordering = ("display_name",)


@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    """Admin configuration for the LessonType model."""

    list_display = (
        "title",
        "tutor",
        "subject",
        "skill_level",
        "duration_minutes",
        "price",
        "is_available",
        "created_at",
    )

    # filters to manage lesson types
    list_filter = (
        "subject",
        "skill_level",
        "is_available",
        "created_at",
    )
    # Search by lesson details or tutor name.
    search_fields = (
        "title",
        "description",
        "tutor__display_name",
    )

    # Present lessons alphabetically.
    ordering = ("title",)
