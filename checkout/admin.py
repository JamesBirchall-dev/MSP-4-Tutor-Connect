from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Payment model.

    Provides a quick visibility of payment status and details.
    Supports filtering and search for efficient admin.
    """

    # Key payment info
    list_display = (
        "booking",
        "amount",
        "created_at",
    )

    # Enables admin users to search by booking ID, student name,
    # and tutor name
    search_fields = (
        "booking__student__username",
        "booking__student__email",
        "booking__lesson_type__title",
    )

    ordering = ("-created_at",)

    list_select_related = (
        "booking",
        "booking__student",
        "booking__lesson_type",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
