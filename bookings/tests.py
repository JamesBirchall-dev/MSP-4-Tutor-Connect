from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from bookings.forms import BookingForm
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


class BookingFormTest(TestCase):

    def test_valid_booking_form(self):
        """
        Test that a Booking form is valid with correct data.
        """
        def test_valid_booking_form(self):
            form = BookingForm(data={
                "booking_date": "2024-06-15",
                "booking_time": "14:00:00",
                "notes": "Hello, I would like to book a lesson."
            })

            self.assertTrue(form.is_valid())


class BookingViewTests(TestCase):

    def test_login_required_for_booking(self):
        response = self.client.get(
            reverse("bookings:booking_create", args=[1]))
        self.assertNotEqual(response.status_code, 200)

    def test_booking_page_loads_for_logged_in_user(self):
        self.client.login(username="student", password="pass")
        response = self.client.get(
            reverse("bookings:booking_create", args=[1]))
        self.assertRedirects(
            response,
            "/accounts/login/?next=/bookings/create/1/"
        )
