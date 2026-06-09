from django.test import TestCase
from django.urls import reverse


class AccountViewTests(TestCase):
    """Tests for the account-related views."""

    def test_register_page_loads_for_anonymous_user(self):
        """Test that the registration page loads for anonymous users."""
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")
# Create your tests here.
