from django.conf import settings
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator


"""
MODELS FOR TUTORS APP
This module contains the data models for the tutors app, including:
- TutorProfile: Extended profile information for tutors.
- LessonType: Represents the types of lessons a tutor can offer.

Relationships:
- One User to One TutorProfile, allowing user to have a unique tutor profile.
- One TutorProfile to many LessonTypes, allowing tutors to offer multiple
lessons.
The models include fields for storing relevant information, such as display
names, bios, experience, lesson subjects, durations, skill levels, and pricing.
"""
# =========================
# TUTOR PROFILE MODEL
# =========================


class TutorProfile(models.Model):
    """
    Represents extended profile information for a tutor.

    This model extends the base user account with tutor-specific data
    such as biography, experience, and profile image.

    Design decisions:
    - Uses OneToOneField with AUTH_USER_MODEL for flexibility
    - Separates authentication data from profile data
    - Allows future expansion without modifying the User model
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

# =========================
# LESSON TYPE MODEL
# =========================
    """
    Represents a type of lesson offered by a tutor.

    Each lesson defines:
    - Subject category
    - Skill level
    - Duration
    - Pricing
    - Availability status
    """


class LessonType(models.Model):
    """
    Represents a type of lesson that a tutor can offer.

    This model allows tutors to specify the subjects or topics they can teach.
    """

    CATEGORY_CHOICES = [
        ("academic", "Academic"),
        ("creative", "Creative Arts"),
        ("languages", "Languages"),
        ("music", "Music"),
        ("technology", "Technology"),
        ("skills", "Study & Life Skills"),
    ]

    SUBJECT_CHOICES = [
        ("mathematics", "Mathematics"),
        ("english", "English"),
        ("science", "General Science"),
        ("biology", "Biology"),
        ("chemistry", "Chemistry"),
        ("physics", "Physics"),
        ("computer_science", "Computer Science"),
        ("history", "History"),
        ("geography", "Geography"),
        ("business_studies", "Business Studies"),
        ("psychology", "Psychology"),

        ("art", "Art"),
        ("design", "Design"),
        ("drama", "Drama"),
        ("photography", "Photography"),

        ("french", "French"),
        ("spanish", "Spanish"),
        ("german", "German"),
        ("italian", "Italian"),
        ("mandarin", "Mandarin Chinese"),
        ("japanese", "Japanese"),
        ("arabic", "Arabic"),

        ("music_theory", "Music Theory"),
        ("piano", "Piano"),
        ("keyboard", "Keyboard"),
        ("guitar_acoustic", "Acoustic Guitar"),
        ("guitar_electric", "Electric Guitar"),
        ("bass_guitar", "Bass Guitar"),
        ("drums", "Drums"),
        ("violin", "Violin"),
        ("voice", "Singing / Vocals"),

        ("coding", "Programming"),
        ("web_development", "Web Development"),
        ("data_science", "Data Science"),

        ("study_skills", "Study Skills"),
        ("exam_preparation", "Exam Preparation"),
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
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="academic",
    )

    subject = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES,
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
        """
        Meta config for LessonType model.
        """
        ordering = ["title"]

    def __str__(self):
        """
        String representation of the LessonType instance.
        """
        return f"{self.tutor.display_name} — {self.title}"
