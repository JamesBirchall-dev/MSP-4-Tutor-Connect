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

    def __str__(self):
        return str(self.user)
