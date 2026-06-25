from django import forms
from .models import TutorProfile, LessonType

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
            "display_name",
            "bio",
            "experience",
            "location",
            "image",
            "is_active",
        ]
        """
        Help tests for form fields to guide users
        in providing the correct information.
        """
        help_texts = {
            "display_name": (
                "The name students will see on your profile."
            ),
            "bio": (
                "Tell students about yourself and your teaching style."
            ),
            "experience": (
                "Summarise your qualifications and teaching experience."
            ),
            "location": (
                "Enter your city, county or 'Online'."
            ),
            "image": (
                "Optional. Upload a JPG, PNG or WebP image up to 5 MB. "
                "Square images work best and will be automatically cropped."
            ),
        }

        widgets = {
            """
            Widgets for form fields for placeholder
            text and input styling.
            """

            "display_name": forms.TextInput(attrs={
                "placeholder": "Jane Smith",
            }),
            "location": forms.TextInput(attrs={
                "placeholder": "London, UK or Online",
            }),
            "bio": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": (
                    "Introduce yourself and describe your teaching style."
                ),
            }),
            "experience": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": (
                    "Grade 8 Guitar, BA Music, 8 years teaching experience..."
                    ),
                }
            ),
        }

    def clean_image(self):

        """
        Custom validation for the image field to ensure uploaded images
        are 5 MB or smaller.
        """
        image = self.cleaned_data.get("image")

        if image and hasattr(image, "size"):
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image must be 5 MB or smaller."
                )

        return image


class LessonTypeForm(forms.ModelForm):
    """
    Form for creating and updating LessonType instances.

    Uses Django's ModelForm to automatically generate form fields
    based on the LessonType model and apply model validation.
    """

    class Meta:
        """
        Meta configuration for the LessonTypeForm.
        """
        model = LessonType
        fields = [
            "title",
            "category",
            "subject",
            "description",
            "lesson_date",
            "lesson_time",
            "duration_minutes",
            "skill_level",
            "price",
            "is_available",
        ]

        widgets = {
            "lesson_date": forms.DateInput(attrs={
                "type": "date",
            }),
            "lesson_time": forms.TimeInput(attrs={
                "type": "time",
            }),
            "description": forms.Textarea(attrs={
                "rows": 5,
            }),
        }
        help_texts = {
            "lesson_date": "Choose the date this lesson will take place.",
            "lesson_time": "Choose the start time for this lesson.",
            "is_available": "Untick this if you want to hide this"
            "lesson from students.",
            }
