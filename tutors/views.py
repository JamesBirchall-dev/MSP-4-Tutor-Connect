from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .models import TutorProfile, LessonType
from .filters import LessonFilter
from django.core.paginator import Paginator
from decimal import Decimal

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
        user = get_object_or_404(User, id=request.POST.get("user"))

        tutor = TutorProfile.objects.create(
            user=user,
            display_name=request.POST.get("display_name"),
            bio=request.POST.get("bio"),
            experience=request.POST.get("experience"),
            location=request.POST.get("location"),
            is_active=True,
        )
        return redirect('tutors:tutor_detail', pk=tutor.pk)

    return render(request, 'tutors/tutor_form.html')


def tutor_update(request, pk):
    # This view is for updating an existing tutor profile.
    tutor = get_object_or_404(TutorProfile, pk=pk)

    if request.method == 'POST':
        tutor.display_name = request.POST.get("display_name")
        tutor.bio = request.POST.get("bio")
        tutor.experience = request.POST.get("experience")
        tutor.location = request.POST.get("location")
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

    queryset = LessonType.objects.select_related("tutor").filter(tutor=tutor)

    lesson_filter = LessonFilter(request.GET, queryset=queryset)

    paginator = Paginator(lesson_filter.qs, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'tutors/lesson_list.html',
        {
            "tutor": tutor,
            "page_obj": page_obj,
            "filter": lesson_filter,
        }
    )


def lesson_create(request, tutor_pk):
    # This view is for creating a new lesson type for a specific tutor.
    tutor = get_object_or_404(TutorProfile, pk=tutor_pk)

    if request.method == 'POST':
        LessonType.objects.create(
            tutor=tutor,
            title=request.POST.get("title"),
            subject=request.POST.get("subject"),
            description=request.POST.get("description", ""),
            duration_minutes=int(request.POST.get("duration_minutes")),
            skill_level=request.POST.get("skill_level"),
            price=Decimal(request.POST.get("price")),
        )
        return redirect('tutors:lesson_list', tutor_pk=tutor.pk)

    return render(request, 'tutors/lesson_form.html', {'tutor': tutor})


def lesson_update(request, tutor_pk, pk):
    # This view is for updating an existing lesson type for a specific tutor.
    tutor = get_object_or_404(TutorProfile, pk=tutor_pk)
    lesson = get_object_or_404(LessonType, pk=pk, tutor=tutor)

    if request.method == 'POST':
        lesson.title = request.POST.get("title")
        lesson.subject = request.POST.get("subject")
        lesson.description = request.POST.get("description", "")
        lesson.duration_minutes = int(request.POST.get("duration_minutes"))
        lesson.skill_level = request.POST.get("skill_level")
        lesson.price = Decimal(request.POST.get("price"))
        lesson.save()
        return redirect('tutors:lesson_list', tutor_pk=tutor.pk)

    return render(
        request, 'tutors/lesson_form.html',
        {'tutor': tutor, 'lesson': lesson})


def lesson_delete(request, tutor_pk, lesson_pk):
    # This view is for deleting a lesson type for a specific tutor.
    tutor = get_object_or_404(TutorProfile, pk=tutor_pk)
    lesson = get_object_or_404(LessonType, pk=lesson_pk, tutor=tutor)

    if request.method == 'POST':
        lesson.delete()
        return redirect('tutors:lesson_list', tutor_pk=tutor.pk)

    return render(
        request, 'tutors/lesson_confirm_delete.html',
        {'tutor': tutor, 'lesson': lesson})
