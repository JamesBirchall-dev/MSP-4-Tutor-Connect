from django import forms
from .models import TutorProfile

"""
FORMS FOR TUTORS APP

This module contains Django forms used for creating and updating
tutor-related data.
"""


class TutorProfileForm(forms.ModelForm):
    """
    Form for creating and updating TutorProfile instances.

    Uses Django's ModelForm to automatically generate form fields
    based on the TutorProfile model and apply model validation.
    """
    class Meta:
        """
        Meta configuration for the TutorProfileForm.
        """
        model = TutorProfile
        fields = [
            "user",
            "display_name",
            "bio",
            "experience",
            "location",
            "image",
            "is_active",
        ]
