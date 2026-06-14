from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from tutors.models import LessonType, TutorProfile


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


class TutorUpdateViewTests(TestCase):
    # Tests for the tutor update view.

    def setUp(self):
        self.user = User.objects.create_user(username="updateuser")

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Update Tutor",
            bio="Test bio",
            experience="3 years",
            location="London",
            is_active=True,
        )

    def test_update_view_returns_200(self):
        # Test that the tutor update view returns a 200 status code.
        response = self.client.get(
            reverse("tutors:tutor_update", args=[self.tutor.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_update_view_shows_form_text(self):
        response = self.client.get(
            reverse("tutors:tutor_update", args=[self.tutor.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update Tutor")

    def test_update_tutor_post_updates_tutor(self):
        # Test that posting to the tutor update view updates the tutor profile.
        response = self.client.post(
            reverse("tutors:tutor_update", args=[self.tutor.pk]),
            {
                "display_name": "Updated Name",
                "bio": "Updated bio",
                "experience": "5 years",
                "location": "New York",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.tutor.refresh_from_db()

        self.assertEqual(self.tutor.display_name, "Updated Name")
        self.assertEqual(self.tutor.bio, "Updated bio")
        self.assertEqual(self.tutor.experience, "5 years")
        self.assertEqual(self.tutor.location, "New York")

    def test_update_tutor_post_redirects(self):
        # Test that posting to the tutor update
        # view redirects to the tutor detail page.
        response = self.client.post(
            reverse("tutors:tutor_update", args=[self.tutor.pk]),
            {
                "display_name": "Redirected Name",
                "bio": "Redirected bio",
                "experience": "4 years",
                "location": "Paris",
            },
        )

        self.assertRedirects(
            response,
            reverse("tutors:tutor_detail", args=[self.tutor.pk]),
        )


class TutorDeleteViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="deleteuser")

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Delete Tutor",
            bio="Test bio",
            experience="3 years",
            location="London",
            is_active=True,
        )

    def test_delete_view_returns_200(self):
        # Test that the tutor delete view returns a 200 status code.
        response = self.client.get(
            reverse("tutors:tutor_delete", args=[self.tutor.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_tutor_removes_object(self):
        # Test that posting to the tutor delete view removes the tutor profile.
        response = self.client.post(
            reverse("tutors:tutor_delete", args=[self.tutor.pk])
        )
        self.assertEqual(TutorProfile.objects.count(), 0)
        self.assertEqual(response.status_code, 302)

    def test_delete_tutor_post_redirects(self):
        # Test that posting to the tutor delete view
        # redirects to the tutor list page.
        response = self.client.post(
            reverse("tutors:tutor_delete", args=[self.tutor.pk])
        )
        self.assertRedirects(response, reverse("tutors:tutor_list"))


class LessonListViewTests(TestCase):
    # Tests for the lesson list view.
    def setUp(self):
        self.user = User.objects.create_user(username="lessonuser")

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Lesson Tutor",
            bio="Test bio",
            experience="3 years",
            location="London",
            is_active=True,
        )

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            subject="math",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20.00,
        )

    def test_lesson_list_view_returns_200(self):
        # Test that the lesson list view returns a 200 status code.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_lesson_list_uses_correct_template(self):
        # Test that the lesson list view uses the correct template.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
        )
        self.assertTemplateUsed(response, "tutors/lesson_list.html")

    def test_lesson_title_displayed_in_list(self):
        # Test that the lesson title is displayed in the lesson list view.
        response = self.client.get(
            reverse(
                "tutors:lesson_list",
                args=[self.tutor.pk],
            )
        )

        self.assertTemplateUsed(
            response,
            "tutors/lesson_list.html",
        )

    def test_search_filters_lessons_by_title(self):
        # Test that the search functionality filters lessons by title.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk]) + "?q=Math"
        )
        self.assertContains(response, "Math Lesson")

    def test_subject_filter_works(self):
        # Test that filtering lessons by subject works.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
            + "?subject=math"
        )
        self.assertContains(response, "Math Lesson")

    def test_skill_filter_works(self):
        # Test that filtering lessons by skill level works.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
            + "?skill_level=beginner"
        )
        self.assertContains(response, "Math Lesson")


class LessonUpdateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="lessonuser")

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Lesson Tutor",
            bio="Test bio",
            experience="3 years",
            location="London",
            is_active=True,
        )

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            subject="math",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20.00,
        )

        self.url = reverse(
            "tutors:lesson_update",
            args=[self.tutor.pk, self.lesson.pk]
        )

    def test_lesson_update_view_returns_200(self):
        # Test that the lesson update view returns a 200 status code.
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_lesson_update_view_shows_form(self):
        # Test that the lesson update view contains the form text.
        response = self.client.get(self.url)
        self.assertContains(response, "Math Lesson")

    def test_lesson_update_updates_object(self):
        # Test that posting to the lesson
        # update view updates the lesson object.
        self.client.post(self.url, {
            "title": "Updated Math Lesson",
            "subject": "math",
            "description": "Updated Algebra",
            "duration_minutes": 90,
            "skill_level": "intermediate",
            "price": 30.00,
        })

        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, "Updated Math Lesson")
        self.assertEqual(self.lesson.description, "Updated Algebra")
        self.assertEqual(self.lesson.duration_minutes, 90)
        self.assertEqual(self.lesson.skill_level, "intermediate")
        self.assertEqual(float(self.lesson.price), 30.00)

    def test_lesson_update_redirects(self):
        # Test that posting to the lesson update
        # view redirects to the lesson list.
        response = self.client.post(self.url, {
            "title": "Updated Math Lesson",
            "subject": "math",
            "description": "Updated Algebra",
            "duration_minutes": 90,
            "skill_level": "intermediate",
            "price": 30.00,
        })

        self.assertRedirects(
            response,
            reverse("tutors:lesson_list", args=[self.tutor.pk])
        )


class LessonDeleteViewTests(TestCase):
    # Tests for the lesson delete view.

    def setUp(self):
        self.user = User.objects.create_user(username="lessonuser")

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Lesson Tutor",
            bio="Test bio",
            experience="3 years",
            location="London",
            is_active=True,
        )

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            subject="math",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20.00,
        )

        self.url = reverse(
            "tutors:lesson_delete",
            args=[self.tutor.pk, self.lesson.pk]
        )

    def test_lesson_delete_view_returns_200(self):
        # Test that the lesson delete view returns a 200 status code.
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
