from django.contrib.auth.models import User
from django.test import TestCase
from tutors.models import TutorProfile

# Create your tests here.


class TutorProfileModelTest(TestCase):
    """Tests for the TutorProfile model."""

    def setUp(self):
        """Set up a user for testing."""
        self.user = User.objects.create_user(
            username="testuser",
            email="tutor@example.com",
            password="testpassword123!",
            )

    def test_tutor_profile_creation(self):
        """Test that a TutorProfile can be created for a user."""
        profile = TutorProfile.objects.create(user=self.user)
        self.assertEqual(profile.user, self.user)
