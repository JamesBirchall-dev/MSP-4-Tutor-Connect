from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tutors.models import LessonType
from .forms import BookingForm
from .models import Booking


@login_required
def booking_create(request, lesson_id):
    """
    Create a new booking for a specific lesson.
    Args:
        lesson_id (int): ID of the lesson to book
    Returns:
        HttpResponse: The HTTP response for the booking creation view
    """

    lesson = get_object_or_404(LessonType, id=lesson_id)
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


def booking_update(request, pk):
    """Display a temporary booking update placeholder view."""
    booking = get_object_or_404(Booking, id=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings:booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/booking_form.html', {
        'form': form,
        'lesson': booking.lesson_type,
        })


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
