from django.conf import settings
from django.db import models

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

    def __str__(self):
        return self.display_name
