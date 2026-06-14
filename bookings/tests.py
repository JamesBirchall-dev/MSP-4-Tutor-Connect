from django.test import TestCase
from django.contrib.auth import get_user_model
from tutors.models import TutorProfile, LessonType
from bookings.models import Booking

User = get_user_model()

"""
Tests for the Booking model.

"""


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuserstudent")
        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online",
            is_active=True,
        )

        self.lesson_type = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Tutoring",
            subject="math",
            skill_level="beginner",
            duration_minutes=60,
            price=50.00,
        )

    def test_booking_creation(self):
        """
        Test that a Booking can be created and has the correct default status.
        """
        booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2024-06-15",
            booking_time="14:00:00",
        )

        self.assertEqual(booking.status, "pending")

        self.assertEqual(
            str(booking),
            f"{self.user} - {self.lesson_type} on 2024-06-15 at 14:00:00"
        )
