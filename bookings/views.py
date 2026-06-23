from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tutors.models import LessonType
from .forms import BookingForm
from .models import Booking


@login_required
def booking_create(request, lesson_pk):
    """
    Create a new booking for a specific lesson.
    Args:
        lesson_pk (int): Primary key of the lesson to book
    Returns:
        HttpResponse: The HTTP response for the booking creation view
    """

    lesson = get_object_or_404(LessonType, id=lesson_pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.student = request.user
            booking.lesson_type = lesson
            booking.save()
            return redirect('bookings:booking_list')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {
        'form': form,
        'lesson': lesson,
        })


@login_required
def booking_list(request):
    """
    Display a list of bookings for the logged-in user.
    Returns:
        HttpResponse: The HTTP response for the booking list view
    """
    bookings = Booking.objects.filter(student=request.user)
    return render(request, 'bookings/booking_list.html', {
        'bookings': bookings,
        })


@login_required
def booking_update(request, pk):
    """ Update an existing booking for the logged-in user."""
    booking = get_object_or_404(
        Booking,
        pk=pk,
        student=request.user
    )

    if booking.status != "pending":
        messages.error(request, "You cannot edit this booking")
        return redirect(
            "bookings:booking_detail",
            pk=booking.pk
        )

    form = BookingForm(
        request.POST or None,
        instance=booking
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Booking updated successfully"
        )
        return redirect(
            "bookings:booking_detail",
            pk=booking.pk
        )

    return render(
        request,
        "bookings/booking_form.html",
        {
            "form": form,
            "booking": booking,
        }
    )


@login_required
def booking_delete(request, pk):
    """Display a temporary booking delete placeholder view."""
    booking = get_object_or_404(Booking, pk=pk, student=request.user)

    if request.method == "POST":
        booking.status = "cancelled"
        booking.save()
        return redirect("bookings:booking_list")

    return render(request, "bookings/confirm_cancel.html", {
        "booking": booking
    })


@login_required
def booking_detail(request, pk):
    """Display the details of a specific booking for the logged-in user.
    Args:
        pk (int): Primary key of the booking to view
    """
    booking = get_object_or_404(Booking, pk=pk, student=request.user)
    return render(request, "bookings/booking_detail.html", {
        "booking": booking
    })
