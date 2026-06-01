from django.http import HttpResponse


def booking_list(request):
    """Display a temporary booking list placeholder view."""
    return HttpResponse("Booking list placeholder")


def booking_create(request, lesson_pk):
    """Display a temporary booking create placeholder view."""
    return HttpResponse(f"Booking create placeholder for lesson {lesson_pk}")


def booking_update(request, pk):
    """Display a temporary booking update placeholder view."""
    return HttpResponse(f"Booking update placeholder for booking {pk}")


def booking_delete(request, pk):
    """Display a temporary booking delete placeholder view."""
    return HttpResponse(f"Booking delete placeholder for booking {pk}")
