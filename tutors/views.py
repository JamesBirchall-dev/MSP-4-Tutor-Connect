from django.shortcuts import redirect, render, get_object_or_404
from .models import TutorProfile, LessonType
from .filters import LessonFilter
from django.core.paginator import Paginator
from decimal import Decimal
from .forms import TutorProfileForm

"""
TUTORS APP VIEWS

This midule contains all view logic for:
- TutorProfile management (list, detail, create, update, delete)
- LessonType management (list, create, update, delete)
- Public tutor browsing and lesson filtering

Each view follows standard Django patterns using function-based views.
"""

# =========================
# TUTOR VIEWS
# =========================


def tutor_list(request):
    """
    Lists all active tutors.

    Filters:
    - Only tutors with is_active=True are shown.

    Template:
    - tutors/tutor_list.html
    """

    tutors = TutorProfile.objects.filter(is_active=True)
    return render(request, 'tutors/tutor_list.html', {'tutors': tutors})


def tutor_detail(request, pk):
    """
    Display details for a single tutor.

    Args:
        pk (int): Primary key of the tutor profile.

    Template:
        tutors/tutor_detail.html
    """
    tutor = get_object_or_404(TutorProfile, pk=pk, is_active=True)
    return render(request, 'tutors/tutor_detail.html', {'tutor': tutor})


def tutor_create(request):
    """
    Create a new tutor profile using TutorProfileForm.

    - Handles GET (empty form)
    - Handles POST (form submission + validation)

    Template:
        tutors/tutor_form.html
    """
    if request.method == "POST":
        form = TutorProfileForm(request.POST, request.FILES)
        if form.is_valid():
            tutor = form.save()
            return redirect("tutors:tutor_detail", pk=tutor.pk)
    else:
        form = TutorProfileForm()

    return render(request, "tutors/tutor_form.html", {"form": form})


def tutor_update(request, pk):
    """
    Update an existing tutor profile.

    Args:
        pk (int): Primary key of the tutor profile to update.

    - Pre-fills form with existing tutor data
    - Saves changes on valid POST submission

    Template:
        tutors/tutor_form.html
    """
    tutor = get_object_or_404(TutorProfile, pk=pk)

    if request.method == "POST":
        tutor.display_name = request.POST["display_name"]
        tutor.bio = request.POST["bio"]
        tutor.experience = request.POST["experience"]
        tutor.location = request.POST["location"]
        tutor.save()

        return redirect("tutors:tutor_detail", pk=tutor.pk)

    return render(
        request,
        "tutors/tutor_form.html",
        {
            "form": TutorProfileForm(instance=tutor),
            "tutor": tutor,
        },
    )


def tutor_delete(request, pk):
    """
    Delete a tutor profile.

    Args:
        pk (int): Primary key of the tutor profile.

    - Confirms deletion on GET
    - Deletes object on POST

    Template:
        tutors/tutor_confirm_delete.html
    """
    tutor = get_object_or_404(TutorProfile, pk=pk)

    if request.method == 'POST':
        tutor.delete()
        return redirect('tutors:tutor_list')

    return render(
        request, 'tutors/tutor_confirm_delete.html', {'tutor': tutor})

# =========================
# LESSON VIEWS
# =========================


def lesson_list(request, tutor_pk):
    """
    Display all lessons for a specific tutor.

    Features:
    - Filtering via LessonFilter
    - Pagination (10 per page)
    - Optimized query using select_related

    Args:
        tutor_pk (int): Primary key of tutor

    Template:
        tutors/lesson_list.html
    """
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
    """
    Create a new lesson type for a specific tutor.

    Args:
        tutor_pk (int): Tutor owning the lesson

    - Handles POST creation
    - Converts numeric fields safely
    """

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
    """
    Update an existing lesson for a tutor.

    Args:
        tutor_pk (int): Tutor ID
        pk (int): Lesson ID
    """
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
    """
    Delete a lesson belonging to a tutor.

    Args:
        tutor_pk (int): Tutor ID
        lesson_pk (int): Lesson ID
    """
    tutor = get_object_or_404(TutorProfile, pk=tutor_pk)
    lesson = get_object_or_404(LessonType, pk=lesson_pk, tutor=tutor)

    if request.method == 'POST':
        lesson.delete()
        return redirect('tutors:lesson_list', tutor_pk=tutor.pk)

    return render(
        request, 'tutors/lesson_confirm_delete.html',
        {'tutor': tutor, 'lesson': lesson})
