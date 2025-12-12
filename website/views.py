from django.shortcuts import render
from .models import Realizacja


def index(request):
    """Strona główna."""
    realizacje = Realizacja.objects.filter(aktywna=True)[:3]
    return render(request, 'website/index.html', {'realizacje': realizacje})


def realizacje(request):
    """Strona z realizacjami."""
    realizacje_list = Realizacja.objects.filter(aktywna=True)
    return render(request, 'website/realizacje.html', {'realizacje': realizacje_list})
