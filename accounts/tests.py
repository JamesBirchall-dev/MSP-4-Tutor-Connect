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
