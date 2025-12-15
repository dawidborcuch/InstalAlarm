# Instrukcja wdrożenia InstalAlarm na produkcję

## 📋 Wymagania

- Python 3.8+
- Django 4.2+
- Serwer WWW (np. Nginx, Apache)
- Serwer aplikacji (np. Gunicorn, uWSGI)
- Baza danych (PostgreSQL zalecana, SQLite dla małych projektów)

---

## 🚀 Krok 1: Przygotowanie środowiska

### 1.1. Sklonuj repozytorium na serwer produkcyjny

```bash
git clone <url-repozytorium>
cd Instalalarm
```

### 1.2. Utwórz środowisko wirtualne

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# lub
venv\Scripts\activate  # Windows
```

### 1.3. Zainstaluj zależności

```bash
pip install -r requirements.txt
```

---

## 🔐 Krok 2: Konfiguracja zmiennych środowiskowych

### 2.1. Utwórz plik .env na serwerze

```bash
cp .env.example .env
nano .env  # lub vim .env
```

### 2.2. Wypełnij plik .env wartościami produkcyjnymi

**WAŻNE:** Wszystkie wartości muszą być ustawione dla produkcji!

```env
# WYGENERUJ NOWY SECRET_KEY!
SECRET_KEY=twoj-wygenerowany-secret-key-tutaj

# DEBUG MUSI być False w produkcji!
DEBUG=False

# Dodaj swoją domenę
ALLOWED_HOSTS=instalalarm.pl,www.instalalarm.pl

# Database (jeśli używasz PostgreSQL)
DATABASE_URL=postgres://user:password@localhost:5432/instalalarm_db

# Email
EMAIL_HOST_USER=ps.instalalarm@gmail.com
EMAIL_HOST_PASSWORD=twoje-haslo-aplikacji-gmail
CONTACT_EMAIL=ps.instalalarm@gmail.com

# Cache (opcjonalnie - Redis dla lepszej wydajności)
CACHE_BACKEND=django.core.cache.backends.locmem.LocMemCache
```

### 2.3. Wygeneruj SECRET_KEY

```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Skopiuj wygenerowany klucz do `.env` jako `SECRET_KEY`.

---

## 🗄️ Krok 3: Konfiguracja bazy danych

### 3.1. Jeśli używasz PostgreSQL

```bash
# Zainstaluj PostgreSQL
sudo apt-get install postgresql postgresql-contrib  # Ubuntu/Debian

# Utwórz bazę danych
sudo -u postgres psql
CREATE DATABASE instalalarm_db;
CREATE USER instalalarm_user WITH PASSWORD 'twoje-haslo';
GRANT ALL PRIVILEGES ON DATABASE instalalarm_db TO instalalarm_user;
\q
```

Zaktualizuj `DATABASE_URL` w `.env`:
```env
DATABASE_URL=postgres://instalalarm_user:twoje-haslo@localhost:5432/instalalarm_db
```

### 3.2. Jeśli używasz SQLite (tylko dla małych projektów)

Nie wymaga dodatkowej konfiguracji - Django utworzy plik automatycznie.

---

## 📦 Krok 4: Migracje i statyczne pliki

### 4.1. Uruchom migracje

```bash
python manage.py migrate
```

### 4.2. Utwórz superużytkownika

```bash
python manage.py createsuperuser
```

### 4.3. Zbierz statyczne pliki

```bash
python manage.py collectstatic --noinput
```

---

## 🔧 Krok 5: Konfiguracja serwera aplikacji (Gunicorn)

### 5.1. Zainstaluj Gunicorn

```bash
pip install gunicorn
```

### 5.2. Utwórz plik gunicorn_config.py

```python
# gunicorn_config.py
bind = "127.0.0.1:8000"
workers = 4
worker_class = "sync"
timeout = 120
keepalive = 5
max_requests = 1000
max_requests_jitter = 50
```

### 5.3. Testuj Gunicorn

```bash
gunicorn --config gunicorn_config.py instalalarm.wsgi:application
```

---

## 🌐 Krok 6: Konfiguracja Nginx (opcjonalne, zalecane)

### 6.1. Utwórz konfigurację Nginx

```nginx
# /etc/nginx/sites-available/instalalarm
server {
    listen 80;
    server_name instalalarm.pl www.instalalarm.pl;

    # Przekierowanie na HTTPS (po skonfigurowaniu SSL)
    # return 301 https://$server_name$request_uri;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /ścieżka/do/projektu/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /ścieżka/do/projektu/media/;
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

### 6.2. Aktywuj konfigurację

```bash
sudo ln -s /etc/nginx/sites-available/instalalarm /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## 🔒 Krok 7: Konfiguracja SSL (Let's Encrypt)

### 7.1. Zainstaluj Certbot

```bash
sudo apt-get install certbot python3-certbot-nginx
```

### 7.2. Uzyskaj certyfikat SSL

```bash
sudo certbot --nginx -d instalalarm.pl -d www.instalalarm.pl
```

Certbot automatycznie zaktualizuje konfigurację Nginx.

---

## 🎯 Krok 8: Konfiguracja systemd (automatyczne uruchamianie)

### 8.1. Utwórz plik systemd service

```bash
sudo nano /etc/systemd/system/instalalarm.service
```

### 8.2. Wypełnij plik:

```ini
[Unit]
Description=InstalAlarm Gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/ścieżka/do/projektu/Instalalarm
Environment="PATH=/ścieżka/do/venv/bin"
ExecStart=/ścieżka/do/venv/bin/gunicorn \
    --config /ścieżka/do/projektu/Instalalarm/gunicorn_config.py \
    instalalarm.wsgi:application

Restart=always

[Install]
WantedBy=multi-user.target
```

### 8.3. Aktywuj i uruchom serwis

```bash
sudo systemctl daemon-reload
sudo systemctl enable instalalarm
sudo systemctl start instalalarm
sudo systemctl status instalalarm
```

---

## 🔄 Krok 9: Aktualizacje (bez psucia produkcji)

### 9.1. Aktualizacja kodu

```bash
# Na serwerze produkcyjnym
cd /ścieżka/do/projektu/Instalalarm
git pull origin main  # lub master
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart instalalarm
```

### 9.2. W środowisku deweloperskim

Możesz normalnie commitować zmiany - nie wpływają one na produkcję, dopóki nie wykonasz `git pull` na serwerze.

---

## ✅ Krok 10: Weryfikacja

### 10.1. Sprawdź logi

```bash
# Logi Gunicorn
sudo journalctl -u instalalarm -f

# Logi Django
tail -f /ścieżka/do/projektu/Instalalarm/logs/django.log

# Logi Nginx
sudo tail -f /var/log/nginx/error.log
```

### 10.2. Testuj aplikację

- Otwórz `https://instalalarm.pl` w przeglądarce
- Sprawdź formularz kontaktowy
- Sprawdź panel admina
- Sprawdź statyczne pliki (CSS, JS)

---

## 🛠️ Rozwiązywanie problemów

### Problem: Błąd 500 Internal Server Error

1. Sprawdź logi: `sudo journalctl -u instalalarm -n 50`
2. Sprawdź `.env` - czy wszystkie zmienne są ustawione?
3. Sprawdź `DEBUG=False` w produkcji
4. Sprawdź uprawnienia do plików: `sudo chown -R www-data:www-data /ścieżka/do/projektu`

### Problem: Statyczne pliki nie ładują się

1. Uruchom: `python manage.py collectstatic --noinput`
2. Sprawdź uprawnienia: `sudo chmod -R 755 staticfiles/`
3. Sprawdź konfigurację Nginx dla `/static/`

### Problem: Błąd bazy danych

1. Sprawdź `DATABASE_URL` w `.env`
2. Sprawdź czy użytkownik bazy danych ma odpowiednie uprawnienia
3. Sprawdź logi PostgreSQL: `sudo tail -f /var/log/postgresql/postgresql-*.log`

---

## 📝 Ważne uwagi

1. **NIGDY nie commituj pliku `.env`** - jest w `.gitignore`
2. **DEBUG musi być False w produkcji** - w przeciwnym razie wyciekają dane wrażliwe
3. **SECRET_KEY musi być unikalny** - wygeneruj nowy dla produkcji
4. **Regularnie aktualizuj zależności** - `pip list --outdated`
5. **Twórz kopie zapasowe bazy danych** - regularnie eksportuj dane
6. **Monitoruj logi** - sprawdzaj błędy regularnie

---

## 🔄 Workflow deweloperski

### Lokalne środowisko (development):
```bash
# Używa instalalarm/settings/development.py
python manage.py runserver
```

### Produkcja:
```bash
# Używa instalalarm/settings/production.py
gunicorn --config gunicorn_config.py instalalarm.wsgi:application
```

**Commity w środowisku deweloperskim NIE wpływają na produkcję** - musisz wykonać `git pull` na serwerze, aby zaktualizować kod.

---

## 📞 Wsparcie

W razie problemów sprawdź:
- Logi aplikacji: `logs/django.log`
- Logi systemowe: `sudo journalctl -u instalalarm`
- Dokumentację Django: https://docs.djangoproject.com/

