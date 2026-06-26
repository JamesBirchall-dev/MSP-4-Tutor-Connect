from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm
from django.utils import timezone
from tutors.models import TutorProfile, LessonType


def register(request):
    """ Allow anyone to create a new account. """
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account was created successfully.")
            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


@login_required
def dashboard(request):
    """ Display the dashboard for logged-in users. """
    tutor_profile = TutorProfile.objects.filter(
        user=request.user
    ).first()

    upcoming_lessons = LessonType.objects.filter(
        tutor=tutor_profile,
        lesson_datee__gte=timezone.now().date(),
        ).order_by(
            "lesson_date",
            "lesson_time",
        )[:3]

    return render(
        request,
        "accounts/dashboard.html",
        {
            "tutor_profile": tutor_profile,
            "upcoming_lessons": upcoming_lessons,
        },
    )
