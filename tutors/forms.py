from django import forms
from .models import TutorProfile

# Form for creating and updating TutorProfile instances


class TutorProfileForm(forms.ModelForm):
    class Meta:
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
