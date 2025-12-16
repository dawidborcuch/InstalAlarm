from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
from django.utils import timezone
from .models import ZdjecieRealizacji, ContactMessage


def index(request):
    """Strona główna."""
    zdjecia = ZdjecieRealizacji.objects.filter(aktywna=True).order_by('-id')
    
    if request.method == 'POST':
        # Rate limiting - max 3 wiadomości na 15 minut z tego samego IP
        ip_address = get_client_ip(request)
        cache_key = f'contact_form_{ip_address}'
        attempts = cache.get(cache_key, 0)
        
        if attempts >= 3:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Zbyt wiele prób. Spróbuj ponownie za 15 minut.'}, status=429)
            messages.error(request, 'Zbyt wiele prób. Spróbuj ponownie za 15 minut.')
            return redirect('index')
        
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
            try:
                # Zapisz do bazy danych
                contact_message = ContactMessage.objects.create(
                    imie=name,
                    telefon=phone,
                    email=email,
                    tresc=message,
                    ip_address=ip_address
                )
                
                # Wyślij email do administratora
                try:
                    send_mail(
                        subject=f'Nowa wiadomość z formularza - {name}',
                        message=f'''
Nowa wiadomość z formularza kontaktowego:

Imię: {name}
Telefon: {phone}
Email: {email}

Treść wiadomości:
{message}

---
Data: {timezone.now().strftime("%Y-%m-%d %H:%M:%S")}
IP: {ip_address}
                        ''',
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.CONTACT_EMAIL],
                        fail_silently=False,
                    )
                    
                    # Wyślij potwierdzenie do klienta
                    send_mail(
                        subject='Potwierdzenie otrzymania wiadomości - InstalAlarm',
                        message=f'''
Dzień dobry {name},

Dziękujemy za kontakt z InstalAlarm!

Otrzymaliśmy Twoją wiadomość i skontaktujemy się z Tobą wkrótce.

Twoja wiadomość:
{message}

---
InstalAlarm Przemysław Stolarz
Jasiorówka 249, 07-130 Jasiorówka
Tel: +48 516 586 323
Email: ps.instalalarm@gmail.com
                        ''',
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email],
                        fail_silently=False,
                    )
                except Exception as e:
                    # Loguj błąd, ale nie przerywaj procesu
                    print(f'Błąd wysyłania emaila: {e}')
                
                # Zwiększ licznik prób
                cache.set(cache_key, attempts + 1, 900)  # 15 minut
                
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.'})
                messages.success(request, 'Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.')
                return redirect('index')
            except Exception as e:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': 'Wystąpił błąd. Spróbuj ponownie później.'}, status=500)
                messages.error(request, 'Wystąpił błąd. Spróbuj ponownie później.')
                return redirect('index')
    
    return render(request, 'website/index.html', {'zdjecia': zdjecia})


def get_client_ip(request):
    """Pobierz adres IP klienta."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def realizacje(request):
    """Strona z realizacjami."""
    zdjecia_list = ZdjecieRealizacji.objects.filter(aktywna=True)
    return render(request, 'website/realizacje.html', {'zdjecia': zdjecia_list})


def polityka_prywatnosci(request):
    """Strona z polityką prywatności."""
    return render(request, 'website/polityka_prywatnosci.html')
