from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form for creating and updating Booking instances.

    Uses Django's ModelForm to automatically generate form fields
    based on the Booking model and apply model validation.
    """
    class Meta:
        """
        Meta configuration for the BookingForm.
        """
        model = Booking
        fields = [
            "booking_date",
            "booking_time",
            "notes",
        ]
