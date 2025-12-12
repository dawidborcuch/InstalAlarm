from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import ZdjecieRealizacji


def index(request):
    """Strona główna."""
    zdjecia = ZdjecieRealizacji.objects.filter(aktywna=True)[:3]
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        privacy = request.POST.get('privacy', False)
        
        # Walidacja
        if not all([name, phone, email, message]):
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Wszystkie pola są wymagane.'})
            messages.error(request, 'Wszystkie pola są wymagane.')
            return redirect('index')
        elif not privacy:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Musisz zaakceptować politykę prywatności.'})
            messages.error(request, 'Musisz zaakceptować politykę prywatności.')
            return redirect('index')
        else:
            # Tutaj możesz dodać zapis do bazy danych lub wysyłanie emaila
            # Na razie tylko komunikat sukcesu
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.'})
            messages.success(request, 'Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.')
            return redirect('index')
    
    return render(request, 'website/index.html', {'zdjecia': zdjecia})


def realizacje(request):
    """Strona z realizacjami."""
    zdjecia_list = ZdjecieRealizacji.objects.filter(aktywna=True)
    return render(request, 'website/realizacje.html', {'zdjecia': zdjecia_list})


def polityka_prywatnosci(request):
    """Strona z polityką prywatności."""
    return render(request, 'website/polityka_prywatnosci.html')
