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
        form = BookingForm(data={
            "booking_date": "2024-06-15",
            "booking_time": "14:00:00",
            "notes": "Hello, I would like to book a lesson."
        })

        self.assertTrue(form.is_valid())


class BookingViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="student",
            password="pass",
        )

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor",
            experience="5 years",
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

    def test_login_required_for_booking(self):
        response = self.client.get(
            reverse("bookings:booking_create", args=[1])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_booking_page_loads_for_logged_in_user(self):
        self.client.login(username="student", password="pass")

        response = self.client.get(
            reverse("bookings:booking_create", args=[1])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book")

    def test_user_can_delete_booking(self):
        self.client.login(username="student", password="pass")

        booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2024-06-15",
            booking_time="14:00:00",
        )

        self.client.post(
            reverse("bookings:booking_delete", args=[booking.id])
        )

        booking.refresh_from_db()
        self.assertEqual(booking.status, "cancelled")


class BookingUpdateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuserstudent",
            password="pass",
        )

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor",
            experience="5 years",
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

        self.booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2024-06-15",
            booking_time="14:00:00",
        )

    def test_booking_update_page_loads(self):
        """Test that the booking update page loads correctly
        for the logged-in user."""
        self.client.login(username="testuserstudent", password="pass")

        response = self.client.get(
            reverse("bookings:booking_update", args=[self.booking.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update Booking")

    def test_booking_can_be_updated(self):
        """Test that a booking can be updated successfully."""
        self.client.login(
            username="testuserstudent",
            password="pass",
        )

        self.client.post(
            reverse(
                "bookings:booking_update",
                args=[self.booking.pk]
            ),
            {
                "booking_date": "2026-08-01",
                "booking_time": "15:00",
                "notes": "Updated notes",
            }
        )

        self.booking.refresh_from_db()

        self.assertEqual(
            str(self.booking.booking_date),
            "2026-08-01"
        )

        self.assertEqual(
            str(self.booking.booking_time),
            "15:00:00"
        )

        self.assertEqual(
            self.booking.notes,
            "Updated notes"
        )


class BookingDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuserstudent",
            password="pass",
        )

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor",
            experience="5 years",
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

        self.booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2024-06-15",
            booking_time="14:00:00",
        )

    def test_booking_detail_page_loads(self):
        """Test that the booking detail page loads
        correctly for the logged-in user.
        """
        self.client.login(username="testuserstudent", password="pass")

        response = self.client.get(
            reverse("bookings:booking_detail", args=[self.booking.pk])
        )

        self.assertEqual(response.status_code, 200)

    def test_booking_detail_requires_login(self):
        response = self.client.get(
            reverse(
                "bookings:booking_detail",
                args=[self.booking.pk]
            )
        )

        self.assertEqual(response.status_code, 302)

    def test_user_cannot_view_another_users_booking(self):
        """Test that a user cannot view another user's booking detail page.
        """
        User.objects.create_user(
            username="otheruser",
            password="pass",
        )
        self.client.login(
            username="otheruser",
            password="pass",
        )

        response = self.client.get(
            reverse(
                "bookings:booking_detail",
                args=[self.booking.pk]
            )
        )

        self.assertEqual(response.status_code, 404)
