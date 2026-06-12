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

    def test_profile_has_timestamps(self):
        """Test that created_at and updated_at fields are set."""
        profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online"
        )
        self.assertIsNotNone(profile.created_at)
        self.assertIsNotNone(profile.updated_at)

    def test_profiles_are_ordered_by_display_name(self):
        """Test that TutorProfiles are ordered by display_name."""

        user1 = User.objects.create_user(
            username="charlie",
            password="testpassword123!",
        )
        user2 = User.objects.create_user(
            username="alice",
            password="testpassword123!",
        )
        user3 = User.objects.create_user(
            username="bob",
            password="testpassword123!",
        )

        profile1 = TutorProfile.objects.create(
            user=user1,
            display_name="Charlie",
            bio="Tutor Charlie.",
            experience="3 years of tutoring experience.",
            location="Online"
        )
        profile2 = TutorProfile.objects.create(
            user=user2,
            display_name="Alice",
            bio="Tutor Alice.",
            experience="4 years of tutoring experience.",
            location="Online"
        )
        profile3 = TutorProfile.objects.create(
            user=user3,
            display_name="Bob",
            bio="Tutor Bob.",
            experience="2 years of tutoring experience.",
            location="Online"
        )
        profiles = TutorProfile.objects.all()
        self.assertEqual(profiles[0], profile2)  # Alice
        self.assertEqual(profiles[1], profile3)  # Bob
        self.assertEqual(profiles[2], profile1)  # Charlie
