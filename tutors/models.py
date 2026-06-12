from django.conf import settings
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
# Create your models here.


class TutorProfile(models.Model):
    """
    Stores extended profile information for a tutor account.

    This model is separate from the user model to:
    - Keep authentication-related fields in the user model.
    - Allow for future expansion of tutor-specific fields without affecting
    the user model.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_profile"
    )
    display_name = models.CharField(max_length=100)
    bio = models.TextField()
    experience = models.TextField()
    location = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to="tutor_profiles/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_name"]

    def __str__(self):
        return self.display_name


class LessonType(models.Model):
    """
    Represents a type of lesson that a tutor can offer.

    This model allows tutors to specify the subjects or topics they can teach.
    """

    SUBJECT_CHOICES = [
        ("math", "Math"),
        ("science", "Science"),
        ("english", "English"),
        ("history", "History"),
        ("language", "Language"),
        ("other", "Other"),
    ]

    SKILL_LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("all_levels", "All Levels"),
    ]

    tutor = models.ForeignKey(
        TutorProfile,
        on_delete=models.CASCADE,
        related_name="lesson_types"
    )
    title = models.CharField(max_length=100)
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        default="other"
    )
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(
        default=60,
        validators=[MinValueValidator(1)]
    )

    skill_level = models.CharField(
        max_length=20,
        choices=SKILL_LEVEL_CHOICES,
        default="all_levels"
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(0)]
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.tutor.display_name} — {self.title}"
