from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountViewTests(TestCase):
    """Tests for the account-related views."""

    def test_register_page_loads_for_anonymous_user(self):
        """Test that the registration page loads for anonymous users."""
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")

    def test_register_page_redirects_for_authenticated_user(self):
        """Test that authenticated users are redirected from the reg page."""
        # Create and log in a test user
        User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123!"
        )

        self.client.login(username="testuser", password="testpassword123!")

        response = self.client.get(reverse("register"))

        self.assertRedirects(response, reverse("dashboard"))

    def test_account_dashboard_page_loads_for_authenticated_user(self):
        """Test that the account dashboard page loads for auth users."""
        # Create and log in a test user
        User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123!"
        )

        self.client.login(username="testuser", password="testpassword123!")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/dashboard.html")
        self.assertContains(response, "My Dashboard")

    def test_registration_rejects_missmatched_passwords(self):
        """Test that registration fails if passwords don't match."""
        response = self.client.post(reverse("register"), {
            "username": "baduser",
            "email": "baduser@example.com",
            "password1": "password123!",
            "password2": "differentpassword456!"
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="baduser").exists())
        self.assertContains(response, "The two password fields didn’t match.")
