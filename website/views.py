from django.shortcuts import render
from .models import ZdjecieRealizacji


def index(request):
    """Strona główna."""
    zdjecia = ZdjecieRealizacji.objects.filter(aktywna=True)[:3]
    return render(request, 'website/index.html', {'zdjecia': zdjecia})


def realizacje(request):
    """Strona z realizacjami."""
    zdjecia_list = ZdjecieRealizacji.objects.filter(aktywna=True)
    return render(request, 'website/realizacje.html', {'zdjecia': zdjecia_list})


def polityka_prywatnosci(request):
    """Strona z polityką prywatności."""
    return render(request, 'website/polityka_prywatnosci.html')
