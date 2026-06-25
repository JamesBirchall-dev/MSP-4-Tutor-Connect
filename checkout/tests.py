import json
from unittest.mock import Mock, patch

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from bookings.tests import User
from tutors.models import TutorProfile, LessonType
from bookings.models import Booking
from checkout.models import Payment
from datetime import time, timedelta
from django.utils import timezone

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

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            category="academic",
            subject="mathematics",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20,
            lesson_date=timezone.now().date() + timedelta(days=7),
            lesson_time=time(14, 0),
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


class CheckoutReviewTests(TestCase):
    def setUp(self):
        self.user = user.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        self.other_user = user.objects.create_user(
            username="otheruser",
            password="otherpassword",
        )

        self.tutor_profile = TutorProfile.objects.create(
            user=self.other_user,
            display_name="Test Tutor",
            bio="This is a test tutor.",
            experience="5 years of teaching experience.",
            location="online",
            is_active=True,
        )

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            category="academic",
            subject="mathematics",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20,
            lesson_date=timezone.now().date() + timedelta(days=7),
            lesson_time=time(14, 0),
        )

        self.booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2023-10-01",
            booking_time="10:00:00",
        )

    def test_checkout_review_requires_login(self):
        """Test that the checkout review view requires login."""
        response = self.client.get(
            reverse("checkout:checkout_review", args=[self.booking.pk])
        )
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_checkout_review_page_loads(self):
        """Test that the checkout review page
        loads correctly for the booking owner."""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.get(
            reverse("checkout:checkout_review", args=[self.booking.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Review Booking")
        self.assertContains(response, "Test Lesson")
        self.assertContains(response, "Test Tutor")
        self.assertContains(response, "£50.00")

    def test_checkout_review_forbidden_for_other_users(self):
        self.client.login(username="otheruser", password="otherpassword")

        response = self.client.get(
            reverse("checkout:checkout_review", args=[self.booking.pk])
        )

        self.assertEqual(response.status_code, 404)
        # Not found for other users


class CheckoutSessionTests(TestCase):
    """Tests for creating Stripe Checkout sessions."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="student@example.com",
        )

        self.tutor_user = User.objects.create_user(
            username="tutoruser",
            password="tutorpassword",
        )

        self.tutor_profile = TutorProfile.objects.create(
            user=self.tutor_user,
            display_name="Test Tutor",
            bio="This is a test tutor.",
            experience="5 years of teaching experience.",
            location="online",
            is_active=True,
        )

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            category="academic",
            subject="mathematics",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20,
            lesson_date=timezone.now().date() + timedelta(days=7),
            lesson_time=time(14, 0),
        )

        self.booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2023-10-01",
            booking_time="10:00:00",
        )

    @patch("checkout.views.stripe.checkout.Session.create")
    def test_create_checkout_session(self, mock_stripe_session_create):
        """Test that a Stripe Checkout session is created."""
        self.client.login(
            username="testuser",
            password="testpassword",
        )

        mock_stripe_session_create.return_value = Mock(
            id="cs_test_123",
            payment_status="unpaid",
            url="https://checkout.stripe.com/test_session",
        )

        response = self.client.post(
            reverse(
                "checkout:create_checkout_session",
                args=[self.booking.pk],
            )
        )

        payment = Payment.objects.get(
            booking=self.booking,
            user=self.user,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            "https://checkout.stripe.com/test_session",
        )

        self.assertEqual(payment.stripe_checkout_id, "cs_test_123")
        self.assertEqual(payment.stripe_payment_status, "unpaid")
        self.assertFalse(payment.paid)

        call_kwargs = mock_stripe_session_create.call_args.kwargs

        self.assertEqual(call_kwargs["mode"], "payment")
        self.assertEqual(call_kwargs["payment_method_types"], ["card"])
        self.assertEqual(call_kwargs["line_items"][0]["quantity"], 1)
        self.assertEqual(
            call_kwargs["line_items"][0]["price_data"]["currency"],
            "gbp",
        )
        self.assertEqual(
            call_kwargs["line_items"][0]["price_data"]["product_data"]["name"],
            self.lesson_type.title,
        )
        self.assertEqual(
            call_kwargs["line_items"][0]["price_data"]["unit_amount"],
            5000,
        )
        self.assertEqual(
            call_kwargs["metadata"]["booking_id"],
            self.booking.pk,
        )
        self.assertEqual(
            call_kwargs["metadata"]["payment_id"],
            payment.pk,
        )


class CheckoutSuccessViewTests(TestCase):
    """Tests for the checkout success view."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

    def test_checkout_success_view(self):
        """Test that the checkout success view loads correctly."""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.get(reverse("checkout:checkout_success"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Payment Successful")
        self.assertContains(
            response,
            "Thank you for your payment. Your booking has been confirmed.",
        )


class CheckoutCancelledViewTests(TestCase):
    """Tests for the checkout cancelled view."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

    def test_checkout_cancelled_view(self):
        """Test that the checkout cancelled view loads correctly."""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.get(reverse("checkout:checkout_cancelled"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Payment Cancelled")
        self.assertContains(
            response,
            "Your payment was not successful."
        )


class StripeWebhookViewTests(TestCase):
    """Tests for the Stripe webhook view."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

        self.tutror_user = User.objects.create_user(
            username="tutoruser",
            password="tutorpassword",
        )

        self.tutor_profile = TutorProfile.objects.create(
            user=self.tutror_user,
            display_name="Test Tutor",
            bio="This is a test tutor.",
            experience="5 years of teaching experience.",
            location="online",
            is_active=True,
        )

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            category="academic",
            subject="mathematics",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20,
            lesson_date=timezone.now().date() + timedelta(days=7),
            lesson_time=time(14, 0),
        )

        self.booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2023-10-01",
            booking_time="10:00:00",
            status="pending",
        )

        self.payment = Payment.objects.create(
            booking=self.booking,
            user=self.user,
            amount=50.00,
            stripe_checkout_id="cs_test_123",
            stripe_payment_status="unpaid",
            paid=False,
        )

    @patch("checkout.views.stripe.Webhook.construct_event")
    def test_checkout_session_completed_marks_as_paid(
        self,
        mock_construct_event,
    ):
        mock_construct_event.return_value = {
            "type": "checkout.session.completed",
            "data": {
                "object": {
                    "id": "cs_test_123",
                    "metadata": {
                        "payment_id": str(self.payment.pk),
                    },
                    "payment_status": "paid",
                }
            },
        }

        response = self.client.post(
            reverse("checkout:stripe_webhook"),
            data=json.dumps({}),
            content_type="application/json",
            HTTP_X_STRIPE_SIGNATURE="test_signature",
        )

        self.payment.refresh_from_db()
        self.booking.refresh_from_db()

        self .assertEqual(response.status_code, 200)
        self.assertTrue(self.payment.paid)
        self.assertEqual(self.payment.stripe_payment_status, "paid")
        self.assertEqual(self.booking.status, "confirmed")
