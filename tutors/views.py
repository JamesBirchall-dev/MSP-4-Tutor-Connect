from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .models import TutorProfile, LessonType

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


def tutor_delete(request, pk):
    # This view is for deleting a tutor profile.
    tutor = get_object_or_404(TutorProfile, pk=pk)

    if request.method == 'POST':
        tutor.delete()
        return redirect('tutors:tutor_list')

    return render(
        request, 'tutors/tutor_confirm_delete.html', {'tutor': tutor})


def lesson_list(request, tutor_pk):
    # This view lists all lesson types for a specific tutor.
    tutor = get_object_or_404(TutorProfile, pk=tutor_pk)
    lessons = LessonType.objects.filter(tutor=tutor)
    return render(
        request, 'tutors/lesson_list.html',
        {'tutor': tutor, 'lessons': lessons})


def lesson_create(request, tutor_pk):
    # This view is for creating a new lesson type for a specific tutor.
    tutor = get_object_or_404(TutorProfile, pk=tutor_pk)

    if request.method == 'POST':
        LessonType.objects.create(
            tutor=tutor,
            title=request.POST["title"],
            subject=request.POST["subject"],
            description=request.POST.get("description", ""),
            duration_minutes=request.POST["duration_minutes"],
            skill_level=request.POST["skill_level"],
            price=request.POST["price"],
        )
        return redirect('tutors:lesson_list', tutor_pk=tutor.pk)

    return render(request, 'tutors/lesson_form.html', {'tutor': tutor})
