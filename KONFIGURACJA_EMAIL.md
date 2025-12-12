# Konfiguracja Email - InstalAlarm

## Jak skonfigurować wysyłanie emaili

### Dla Gmaila (najprostsze rozwiązanie)

1. **EMAIL_HOST_USER** - Twój email Gmail
   - Przykład: `przemyslaw.stolarz@gmail.com`
   - To jest email, z którego będą wysyłane wiadomości

2. **EMAIL_HOST_PASSWORD** - Hasło aplikacji Gmail (NIE zwykłe hasło!)
   - Gmail wymaga użycia "hasła aplikacji" zamiast zwykłego hasła
   - Jak utworzyć hasło aplikacji:
     - Wejdź na: https://myaccount.google.com/apppasswords
     - Zaloguj się swoim kontem Google
     - Wybierz "Aplikacja": Poczta
     - Wybierz "Urządzenie": Komputer (lub inne)
     - Kliknij "Generuj"
     - Skopiuj wygenerowane hasło (16 znaków, np. `abcd efgh ijkl mnop`)
     - Wpisz to hasło w `EMAIL_HOST_PASSWORD` (bez spacji: `abcdefghijklmnop`)

3. **CONTACT_EMAIL** - Email, na który będą przychodzić wiadomości z formularza
   - Może być ten sam co `EMAIL_HOST_USER`
   - Przykład: `przemyslaw.stolarz@gmail.com`
   - To jest email, na który będą przychodzić wiadomości od klientów

### Przykładowa konfiguracja w settings.py:

```python
EMAIL_HOST_USER = 'przemyslaw.stolarz@gmail.com'
EMAIL_HOST_PASSWORD = 'abcdefghijklmnop'  # Hasło aplikacji (16 znaków)
CONTACT_EMAIL = 'przemyslaw.stolarz@gmail.com'
```

### Dla własnej domeny (np. ps.instalalarm@gmail.com)

Jeśli masz własną domenę i serwer email:

```python
EMAIL_HOST = 'smtp.instalalarm.pl'  # lub inny serwer SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ps.instalalarm@gmail.com'
EMAIL_HOST_PASSWORD = 'twoje-haslo-do-konta-email'
CONTACT_EMAIL = 'ps.instalalarm@gmail.com'
```

### Testowanie

Po skonfigurowaniu możesz przetestować wysyłanie emaili:

1. Uruchom serwer Django: `python manage.py runserver`
2. Wejdź na stronę i wyślij formularz kontaktowy
3. Sprawdź:
   - Czy email przyszedł na `CONTACT_EMAIL` (wiadomość od klienta)
   - Czy klient otrzymał email potwierdzający (na email podany w formularzu)

### Ważne uwagi:

- **Dla Gmaila**: Zawsze używaj hasła aplikacji, nie zwykłego hasła!
- **Bezpieczeństwo**: W produkcji nie przechowuj haseł w settings.py - użyj zmiennych środowiskowych
- **Spam**: Gmail może oznaczyć pierwsze emaile jako spam - sprawdź folder Spam

