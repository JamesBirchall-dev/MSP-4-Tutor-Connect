from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from bookings.models import Booking


def checkout(request, booking_pk):
    """Display a temporary checkout placeholder view."""
    return HttpResponse(f"Checkout placeholder for booking {booking_pk}")


def create_checkout_session(request, booking_pk):
    """Display a temporary Stripe checkout session placeholder view."""
    msg = f"Checkout session placeholder for booking {booking_pk}"
    return HttpResponse(msg)


@login_required
def checkout_review(request, booking_pk):
    """Display a review page for the booking before proceeding to payment."""
    booking = get_object_or_404(Booking, pk=booking_pk, user=request.user)
    return render(
        request,
        "checkout/checkout_review.html",
        {"booking": booking},
    )


def checkout_success(request):
    """Display a temporary checkout success placeholder view."""
    return HttpResponse("Checkout success placeholder")


def checkout_cancelled(request):
    """Display a temporary checkout cancelled placeholder view."""
    return HttpResponse("Checkout cancelled placeholder")
