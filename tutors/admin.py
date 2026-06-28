from django.contrib import admin
from tutors.models import LessonType, TutorProfile

"""
ADMIN CONFIGURATION FOR TUTORS APP

This module customises the Django admin interface for:
- Tutor profiles
- Lesson types

Provides filtering, searching, ordering, and optimised query
performance for admin users.
"""

# =========================
# TUTOR PROFILE ADMIN
# =========================


@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TutorProfile model.

    Provides a quick visibility of tutor status and profile info.
    Supports filtering and search for efficient admin.
    """

    # Key profile info
    list_display = (
        "display_name",
        "user",
        "location",
        "contact_email",
        "is_active",
        "created_at",
    )

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
        "contact_email",
        "lesson_delivery_info",
    )

    # Display profiles alphabetically by display name
    ordering = ("display_name",)

    # Auto-managed timestamps are read-only in the admin interface
    readonly_fields = (
        "created_at",
        "updated_at",
    )


# =========================
# LESSON TYPE ADMIN
# =========================

@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for LessonType.

    Features:
    - Search by lesson details and tutor
    - Filter by subject, skill level, and availability
    - Optimised tutor lookup using select_related
    - Read-only audit timestamps
    """

    list_display = (
        "title",
        "tutor",
        "category",
        "subject",
        "skill_level",
        "lesson_date",
        "lesson_time",
        "duration_minutes",
        "price",
        "is_available",
    )

    # filters to manage lesson types
    list_filter = (
        "category",
        "subject",
        "skill_level",
        "is_available",
        "lesson_date",
        "created_at",
    )
    # Search by lesson details or tutor name.
    search_fields = (
        "title",
        "description",
        "tutor__display_name",
    )

    # Present lessons alphabetically.
    ordering = ("lesson_date", "lesson_time")

    # optimised tutor lookup to reduce database queries in the admin list view.
    list_select_related = ("tutor",)

    # auto-managed timestamps are read-only in the admin interface
    readonly_fields = (
        "created_at",
        "updated_at",
    )
