from django.conf import settings
from django.db import models
from tutors.models import LessonType
"""
Booking model for managing student lesson bookings.
This model represents a booking made by a student for a specific lesson type
offered by a tutor. It includes details such as the student, lesson type,
booking date and time, status, and optional notes.

"""


class Booking(models.Model):
    """
    Represents a booking made by a student for a lesson type.
    """
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    lesson_type = models.ForeignKey(
        LessonType,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    booking_date = models.DateField()
    booking_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.student} - "
            f"{self.lesson_type} on "
            f"{self.booking_date} at "
            f"{self.booking_time}"
        )
