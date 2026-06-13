from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
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
    # This view is for creating a new tutor profile.
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.POST["user"])

        tutor = TutorProfile.objects.create(
            user=user,
            display_name=request.POST["display_name"],
            bio=request.POST["bio"],
            experience=request.POST["experience"],
            location=request.POST["location"],
            is_active=True,
        )
        return redirect('tutors:tutor_detail', pk=tutor.pk)

    return render(request, 'tutors/tutor_form.html')


def tutor_update(request, pk):
    # This view is for updating an existing tutor profile.
    tutor = get_object_or_404(TutorProfile, pk=pk)

    if request.method == 'POST':
        tutor.display_name = request.POST["display_name"]
        tutor.bio = request.POST["bio"]
        tutor.experience = request.POST["experience"]
        tutor.location = request.POST["location"]
        tutor.save()
        return redirect('tutors:tutor_detail', pk=tutor.pk)

    return render(request, 'tutors/tutor_form.html', {'tutor': tutor})

