from django.test import TestCase
from django.contrib.auth import get_user_model
from tutors.models import TutorProfile, LessonType
from bookings.models import Booking
from checkout.models import Payment

user = get_user_model()

"""Tests for the checkout app."""


class PaymentModelTestCase(TestCase):
    """Test case for the Payment model."""
    def setUp(self):
        self.user = user.objects.create_user(
            username="testuser",
            password="testpassword",
        )

        self.tutor_profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="This is a test tutor.",
            experience="5 years of teaching experience.",
            location="online",
            is_active=True,
        )

        self.lesson_type = LessonType.objects.create(
            tutor=self.tutor_profile,
            title="Test Lesson",
            subject="math",
            skill_level="beginner",
            duration_minutes=60,
            price=50.00,
        )

        self.booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2023-10-01",
            booking_time="10:00:00",
        )

    def test_payment_creation(self):
        """Test the creation of a Payment instance."""
        payment = Payment.objects.create(
            booking=self.booking,
            user=self.user,
            amount=50.00,
        )

        self.assertEqual(payment.amount, 50.00)
        self.assertFalse(payment.paid)

    def test_payment_str_representation(self):
        """Test the string representation of the Payment model."""
        payment = Payment.objects.create(
            booking=self.booking,
            user=self.user,
            amount=50.00,
        )

        self.assertEqual(
            str(payment),
            f"{self.user} - {self.booking} - £{payment.amount}",
        )
