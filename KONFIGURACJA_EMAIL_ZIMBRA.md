# Konfiguracja Email - Zimbra OVH

## 📧 Konfiguracja dla Zimbra Email z OVH

### Parametry SMTP dla Zimbra OVH:

- **SMTP Host:** `ssl0.ovh.net`
- **Port:** `587` (TLS) lub `465` (SSL)
- **Używa TLS:** `True` (dla portu 587) lub `False` (dla portu 465)
- **Używa SSL:** `False` (dla portu 587) lub `True` (dla portu 465)
- **Użytkownik:** `kontakt@instalalarm.pl` (pełny adres email)
- **Hasło:** Hasło do konta email w Zimbra OVH

---

## 🔧 Konfiguracja w pliku .env

Na serwerze edytuj plik `.env`:

```bash
nano /home/ubuntu/InstalAlarm/.env
```

Ustaw następujące wartości:

```env
# Email Configuration - Zimbra OVH
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=ssl0.ovh.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_USER=kontakt@instalalarm.pl
EMAIL_HOST_PASSWORD=twoje-haslo-do-konta-zimbra
DEFAULT_FROM_EMAIL=InstalAlarm <kontakt@instalalarm.pl>
CONTACT_EMAIL=ps.instalalarm@gmail.com
```

**WAŻNE:**
- `EMAIL_HOST_USER` - to jest nadawca (kontakt@instalalarm.pl)
- `CONTACT_EMAIL` - to jest odbiorca (ps.instalalarm@gmail.com) - tutaj będą przychodzić wiadomości z formularza

---

## 🔄 Alternatywna konfiguracja (Port 465 z SSL)

Jeśli port 587 nie działa, użyj portu 465 z SSL:

```env
EMAIL_HOST=ssl0.ovh.net
EMAIL_PORT=465
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
EMAIL_HOST_USER=kontakt@instalalarm.pl
EMAIL_HOST_PASSWORD=twoje-haslo-do-konta-zimbra
DEFAULT_FROM_EMAIL=InstalAlarm <kontakt@instalalarm.pl>
CONTACT_EMAIL=ps.instalalarm@gmail.com
```

---

## ✅ Testowanie konfiguracji

Po zaktualizowaniu `.env`, zrestartuj aplikację:

```bash
sudo systemctl restart instalalarm
```

Następnie możesz przetestować wysyłkę email przez Django shell:

```bash
source venv/bin/activate
python manage.py shell
```

W konsoli Pythona:

```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    subject='Test email z InstalAlarm',
    message='To jest testowa wiadomość.',
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[settings.CONTACT_EMAIL],
    fail_silently=False,
)
```

Jeśli email dotrze do `ps.instalalarm@gmail.com`, konfiguracja działa poprawnie!

---

## 📝 Jak to działa

1. **Klient wypełnia formularz** na stronie
2. **Aplikacja wysyła email** z konta `kontakt@instalalarm.pl` (Zimbra OVH)
3. **Email trafia do** `ps.instalalarm@gmail.com` (Gmail)
4. **Klient otrzymuje potwierdzenie** na swój adres email (ten, który podał w formularzu)

---

## 🛠️ Rozwiązywanie problemów

### Problem: Błąd "Authentication failed"

- Sprawdź, czy hasło jest poprawne
- Upewnij się, że używasz pełnego adresu email jako `EMAIL_HOST_USER`
- Sprawdź, czy konto email jest aktywne w panelu OVH

### Problem: Błąd "Connection timeout"

- Sprawdź, czy port 587 jest otwarty w firewall
- Spróbuj portu 465 z SSL zamiast 587 z TLS

### Problem: Email nie dociera

- Sprawdź folder SPAM w Gmail
- Sprawdź logi Django: `tail -f /home/ubuntu/InstalAlarm/logs/django.log`
- Sprawdź logi Gunicorn: `sudo journalctl -u instalalarm -f`

---

## 📞 Wsparcie

W razie problemów sprawdź dokumentację OVH:
- https://docs.ovh.com/pl/emails/

