from django.shortcuts import render, get_object_or_404
from .models import TutorProfile

"""
Views for the tutors app.
These functions handle the logic for displaying tutor profiles and details.
"""


def tutor_list(request):
    tutors = TutorProfile.objects.filter(is_active=True)
    return render(request, 'tutors/tutor_list.html', {'tutors': tutors})


def tutor_detail(request, pk):
    tutor = get_object_or_404(TutorProfile, pk=pk, is_active=True)
    return render(request, 'tutors/tutor_detail.html', {'tutor': tutor})


def tutor_create(request):
    # Placeholder for tutor creation logic
    return render(request, 'tutors/tutor_form.html', {})
