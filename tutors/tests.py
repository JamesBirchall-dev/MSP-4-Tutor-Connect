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

    def test_tutor_profile_stores_information(self):
        """Test that TutorProfile can store and retrieve information."""
        profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online"
        )
        self.assertEqual(profile.display_name, "Test Tutor")
        self.assertEqual(profile.bio, "Experienced tutor in math and science.")
        self.assertEqual(profile.experience, "5 years of tutoring experience.")
        self.assertEqual(profile.location, "Online")

    def test_image_field_is_optional(self):
        """Test that the image field can be left blank."""
        profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online"
        )
        self.assertFalse(profile.image)

    def test_is_active_default(self):
        """Test that the is_active field defaults to True."""
        profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online"
        )
        self.assertTrue(profile.is_active)
