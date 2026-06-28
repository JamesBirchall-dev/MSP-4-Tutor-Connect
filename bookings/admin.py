from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.

    Provides a quick visibility of booking status and details.
    Supports filtering and search for efficient admin.
    """

    # Key booking info
    list_display = (
        "student",
        "lesson_type",
        "booking_date",
        "booking_time",
        "status",
        "created_at",
    )

    # Filters to manage bookings by status and date
    list_filter = ("status", "booking_date", "created_at")

    # Enables admin users to search by student name,
    # lesson title, and tutor name
    search_fields = (
        "student__username",
        "student__email",
        "lesson_type__title",
        "lesson_type__tutor__display_name",
        "notes",
    )

    ordering = ("booking_date", "booking_time")

    list_select_related = ("student", "lesson_type", "lesson_type__tutor")

    readonly_fields = (
        "created_at",
        "updated_at",
    )
