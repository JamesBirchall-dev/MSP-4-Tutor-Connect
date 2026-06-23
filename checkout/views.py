import stripe

from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from bookings.models import Booking
from .models import Payment


def checkout(request, booking_pk):
    """Display a temporary checkout placeholder view."""
    return HttpResponse(f"Checkout placeholder for booking {booking_pk}")


@login_required
def create_checkout_session(request, booking_pk):
    """Create a Stripe Checkout session for the booking."""
    booking = get_object_or_404(
        Booking,
        pk=booking_pk,
        student=request.user,
    )

    payment, created = Payment.objects.get_or_create(
        booking=booking,
        user=request.user,
        defaults={"amount": booking.lesson_type.price},
    )

    stripe.api_key = settings.STRIPE_SECRET_KEY

    success_url = request.build_absolute_uri(
        reverse("checkout:checkout_success")
    )

    cancel_url = request.build_absolute_uri(
        reverse("checkout:checkout_cancelled")
    )

    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {
                        "name": booking.lesson_type.title,
                    },
                    "unit_amount": int(booking.lesson_type.price * 100),
                },
                "quantity": 1,
            }
        ],
        metadata={
            "booking_id": booking.id,
            "payment_id": payment.id,
        },
        success_url=success_url,
        cancel_url=cancel_url,
    )

    payment.stripe_checkout_id = session.id
    payment.stripe_payment_status = session.payment_status
    payment.save()
    return redirect(session.url)


@login_required
def checkout_review(request, booking_pk):
    """Display a review page for the booking before proceeding to payment."""
    booking = get_object_or_404(Booking, pk=booking_pk, student=request.user)
    return render(
        request,
        "checkout/checkout_review.html",
        {"booking": booking},
    )


def checkout_success(request):
    """Display a payment success page after a successful checkout."""
    return render(request, "checkout/checkout_success.html")


def checkout_cancelled(request):
    """Display a temporary checkout cancelled placeholder view."""
    return HttpResponse("Checkout cancelled placeholder")
