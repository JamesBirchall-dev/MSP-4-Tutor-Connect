from django.http import HttpResponse


def checkout(request, booking_pk):
    """Display a temporary checkout placeholder view."""
    return HttpResponse(f"Checkout placeholder for booking {booking_pk}")


def create_checkout_session(request, booking_pk):
    """Display a temporary Stripe checkout session placeholder view."""
    msg = f"Checkout session placeholder for booking {booking_pk}"
    return HttpResponse(msg)


def checkout_success(request):
    """Display a temporary checkout success placeholder view."""
    return HttpResponse("Checkout success placeholder")


def checkout_cancelled(request):
    """Display a temporary checkout cancelled placeholder view."""
    return HttpResponse("Checkout cancelled placeholder")
