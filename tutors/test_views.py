from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from tutors.models import TutorProfile


class TutorListViewTests(TestCase):
    """Tests for the views in the tutors app."""

    def setUp(self):
        """Set up a user and tutor profile for testing."""
        self.user = User.objects.create_user(
            username="testuser",
        )

        self.active_tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Active Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online",
            is_active=True
        )

        self.inactive_tutor = TutorProfile.objects.create(
            user=User.objects.create(username="inactiveuser"),
            display_name="Inactive Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online",
            is_active=False
        )

    def test_tutor_list_status_code(self):
        """Test that the tutor list view returns a 200 status code."""
        response = self.client.get(reverse('tutors:tutor_list'))
        self.assertEqual(response.status_code, 200)

    def test_only_active_tutors_in_list(self):
        """Test that only active tutors are displayed in the tutor list."""
        response = self.client.get(reverse("tutors:tutor_list"))
        self.assertContains(response, "Active Tutor")
        self.assertNotContains(response, "Inactive Tutor")

    def test_correct_template_used(self):
        response = self.client.get(reverse("tutors:tutor_list"))
        self.assertTemplateUsed(response, "tutors/tutor_list.html")


class TutorDetailViewTests(TestCase):
    """Tests for the tutor detail view."""

    def setUp(self):
        """Set up a user and tutor profile for testing."""
        self.user = User.objects.create_user(
            username="testuser",
        )

        self.active_tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Active Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online",
            is_active=True
        )

        self.inactive_tutor = TutorProfile.objects.create(
            user=User.objects.create(username="inactiveuser"),
            display_name="Inactive Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online",
            is_active=False
        )

    def test_tutor_detail_status_code(self):
        """Test that the tutor detail view returns
        a 200 status code for an active tutor."""
        response = self.client.get(reverse("tutors:tutor_detail",
                                           args=[self.active_tutor.pk]))
        self.assertEqual(response.status_code, 200)

    def test_inactive_tutor_detail_returns_404(self):
        """Test that the tutor detail view returns
        a 404 status code for an inactive tutor."""
        response = self.client.get(reverse("tutors:tutor_detail",
                                           args=[self.inactive_tutor.pk]))
        self.assertEqual(response.status_code, 404)

    def test_correct_template_used(self):
        response = self.client.get(reverse("tutors:tutor_detail",
                                           args=[self.active_tutor.pk]))
        self.assertTemplateUsed(response, "tutors/tutor_detail.html")


class TutorCreateViewTests(TestCase):

    def test_create_view_returns_200(self):
        # Test that the tutor create view returns a 200 status code.
        response = self.client.get(reverse("tutors:tutor_create"))
        self.assertEqual(response.status_code, 200)

    def test_create_view_shows_form_text(self):
        # Test that the tutor create view contains the form text.
        response = self.client.get(reverse("tutors:tutor_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Tutor")

    def test_create_tutor_post_creates_tutor(self):
        # Test that posting to the tutory
        # create view creates a new tutor profile.
        user = User.objects.create_user(username="newuser")

        self.client.post(reverse("tutors:tutor_create"), {
            "user": user.id,
            "display_name": "New Tutor",
            "bio": "Test bio",
            "experience": "3 years",
            "location": "London",
            "is_active": True
        })

        self.assertEqual(TutorProfile.objects.count(), 1)

        tutor = TutorProfile.objects.first()
        self.assertEqual(tutor.display_name, "New Tutor")

    def test_create_tutor_post_redirects(self):
        # Test that posting to the tutor create
        # view redirects to the tutor detail page.
        user = User.objects.create_user(username="newuser")

        response = self.client.post(reverse("tutors:tutor_create"), {
            "user": user.id,
            "display_name": "Redirect Tutor",
            "bio": "Test bio",
            "experience": "3 years",
            "location": "London",
            "is_active": True
        })

        tutor = TutorProfile.objects.get(display_name="Redirect Tutor")
        self.assertRedirects(
            response,
            reverse("tutors:tutor_detail", args=[tutor.pk])
        )
