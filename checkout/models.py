from django.conf import settings
from django.db import models

from bookings.models import Booking


class Payment(models.Model):
    """
    Model to store payment information for a booking.
    """

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="payment",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="payments",
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The amount paid for the booking.",
    )

    stripe_checkout_id = models.CharField(
        max_length=255,
        blank=True,
        help_text="The Stripe Checkout session ID for the payment.",

    )

    stripe_payment_status = models.CharField(
        max_length=50,
        blank=True,
        help_text="The status of the payment in Stripe.",
    )

    paid = models.BooleanField(
        default=False,
        help_text="Indicates whether the payment has been completed.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.booking} - £{self.amount}"
