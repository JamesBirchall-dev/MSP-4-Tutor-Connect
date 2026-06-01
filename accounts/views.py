from django.http import HttpResponse


def register(request):
    """Display a temporary registration placeholder view."""
    return HttpResponse("Register view placeholder")


def dashboard(request):
    """Display a temporary dashboard placeholder view."""
    return HttpResponse("Dashboard view placeholder")
