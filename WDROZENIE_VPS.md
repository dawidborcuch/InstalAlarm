# 🚀 Wdrożenie InstalAlarm na VPS (Ubuntu 22.04)

**Adres serwera:** 145.239.90.136  
**System:** Ubuntu 22.04

---

## 📋 Krok 1: Przygotowanie serwera

### 1.1. Aktualizacja systemu

```bash
sudo apt update
sudo apt upgrade -y
```

### 1.2. Instalacja podstawowych narzędzi

```bash
sudo apt install -y git curl wget build-essential python3-pip python3.10-venv python3-venv nginx
```

**UWAGA:** Jeśli widzisz błąd "ensurepip is not available", zainstaluj:
```bash
sudo apt install -y python3.10-venv
```

### 1.3. Instalacja PostgreSQL (zalecane dla produkcji)

```bash
sudo apt install -y postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 1.4. Utworzenie użytkownika dla aplikacji (opcjonalne, ale zalecane)

```bash
sudo adduser --disabled-password --gecos "" instalalarm
sudo usermod -aG sudo instalalarm
```

---

## 📦 Krok 2: Sklonowanie repozytorium

### 2.1. Przejdź do katalogu użytkownika

```bash
cd /home/instalalarm  # lub cd ~ jeśli używasz swojego użytkownika
```

### 2.2. Sklonuj repozytorium

```bash
git clone <URL-TWOJEGO-REPOZYTORIUM> Instalalarm
cd Instalalarm
```

**Jeśli nie masz repozytorium Git:**
```bash
# Utwórz katalog
mkdir -p /home/instalalarm/Instalalarm
cd /home/instalalarm/Instalalarm
# Następnie prześlij pliki przez SCP/SFTP z lokalnego komputera
```

---

## 🐍 Krok 3: Konfiguracja Pythona

### 3.1. Utwórz środowisko wirtualne

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3.2. Zainstaluj zależności

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔐 Krok 4: Konfiguracja zmiennych środowiskowych

### 4.1. Utwórz plik .env

```bash
cp .env.example .env
nano .env
```

### 4.2. Wypełnij plik .env następującymi wartościami:

```env
# Django Settings
SECRET_KEY=WYGENERUJ-NOWY-KLUCZ-PONIZEJ
DEBUG=False
ALLOWED_HOSTS=145.239.90.136,instalalarm.pl,www.instalalarm.pl

# Database (PostgreSQL)
DATABASE_URL=postgres://instalalarm_user:twoje_haslo_bazy@localhost:5432/instalalarm_db

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=ps.instalalarm@gmail.com
EMAIL_HOST_PASSWORD=twoje-haslo-aplikacji-gmail
DEFAULT_FROM_EMAIL=InstalAlarm <ps.instalalarm@gmail.com>
CONTACT_EMAIL=ps.instalalarm@gmail.com

# Cache
CACHE_BACKEND=django.core.cache.backends.locmem.LocMemCache
```

### 4.3. Wygeneruj SECRET_KEY

```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Skopiuj wygenerowany klucz i wklej jako `SECRET_KEY` w pliku `.env`.

---

## 🗄️ Krok 5: Konfiguracja bazy danych PostgreSQL

### 5.1. Sprawdź czy PostgreSQL jest zainstalowany

```bash
sudo systemctl status postgresql
```

Jeśli PostgreSQL nie jest zainstalowany, zainstaluj go:
```bash
sudo apt install -y postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 5.2. Sprawdź użytkownika PostgreSQL

W Ubuntu 22.04 PostgreSQL może używać innego użytkownika. Sprawdź:
```bash
sudo -u postgres psql
```

Jeśli to nie działa, spróbuj:
```bash
sudo su - postgres
psql
```

Lub sprawdź jaki użytkownik jest używany:
```bash
ps aux | grep postgres
```

### 5.3. Przejdź do PostgreSQL

```bash
sudo -u postgres psql
```

### 5.2. Utwórz bazę danych i użytkownika

```sql
CREATE DATABASE instalalarm_db;
CREATE USER instalalarm_user WITH PASSWORD 'twoje_silne_haslo_tutaj';
ALTER ROLE instalalarm_user SET client_encoding TO 'utf8';
ALTER ROLE instalalarm_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE instalalarm_user SET timezone TO 'Europe/Warsaw';
GRANT ALL PRIVILEGES ON DATABASE instalalarm_db TO instalalarm_user;
\q
```

### 5.3. Zaktualizuj DATABASE_URL w .env

Zmień `DATABASE_URL` w pliku `.env` na:
```env
DATABASE_URL=postgres://instalalarm_user:twoje_silne_haslo_tutaj@localhost:5432/instalalarm_db
```

---

## 📦 Krok 6: Migracje i statyczne pliki

### 6.1. Uruchom migracje

```bash
source venv/bin/activate
python manage.py migrate
```

### 6.2. Utwórz superużytkownika

```bash
python manage.py createsuperuser
```

### 6.3. Zbierz statyczne pliki

```bash
python manage.py collectstatic --noinput
```

---

## 🔧 Krok 7: Konfiguracja Gunicorn

### 7.1. Testuj Gunicorn

```bash
source venv/bin/activate
gunicorn --config gunicorn_config.py instalalarm.wsgi:application
```

Powinieneś zobaczyć, że Gunicorn działa. Naciśnij `Ctrl+C`, aby zatrzymać.

### 7.2. Utwórz katalog dla logów

```bash
mkdir -p logs
```

---

## 🎯 Krok 8: Konfiguracja systemd (automatyczne uruchamianie)

### 8.1. Utwórz plik serwisu

```bash
sudo nano /etc/systemd/system/instalalarm.service
```

### 8.2. Wklej następującą konfigurację:

```ini
[Unit]
Description=InstalAlarm Gunicorn daemon
After=network.target postgresql.service

[Service]
User=instalalarm
Group=www-data
WorkingDirectory=/home/instalalarm/Instalalarm
Environment="PATH=/home/instalalarm/Instalalarm/venv/bin"
EnvironmentFile=/home/instalalarm/Instalalarm/.env
ExecStart=/home/instalalarm/Instalalarm/venv/bin/gunicorn \
    --config /home/instalalarm/Instalalarm/gunicorn_config.py \
    instalalarm.wsgi:application

Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

**WAŻNE:** Zmień ścieżki jeśli używasz innego użytkownika lub katalogu!

### 8.3. Aktywuj i uruchom serwis

```bash
sudo systemctl daemon-reload
sudo systemctl enable instalalarm
sudo systemctl start instalalarm
sudo systemctl status instalalarm
```

Powinieneś zobaczyć `active (running)`. Jeśli są błędy, sprawdź:
```bash
sudo journalctl -u instalalarm -n 50
```

---

## 🌐 Krok 9: Konfiguracja Nginx

### 9.1. Utwórz konfigurację Nginx

```bash
sudo nano /etc/nginx/sites-available/instalalarm
```

### 9.2. Wklej następującą konfigurację:

```nginx
server {
    listen 80;
    server_name 145.239.90.136 instalalarm.pl www.instalalarm.pl;

    # Logi
    access_log /var/log/nginx/instalalarm_access.log;
    error_log /var/log/nginx/instalalarm_error.log;

    # Maksymalny rozmiar uploadu
    client_max_body_size 20M;

    # Statyczne pliki
    location /static/ {
        alias /home/instalalarm/Instalalarm/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Pliki media
    location /media/ {
        alias /home/instalalarm/Instalalarm/media/;
        expires 7d;
        add_header Cache-Control "public";
    }

    # Proxy do Gunicorn
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        
        # Timeout dla długich żądań
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

**WAŻNE:** Zmień ścieżki jeśli używasz innego katalogu!

### 9.3. Aktywuj konfigurację

```bash
sudo ln -s /etc/nginx/sites-available/instalalarm /etc/nginx/sites-enabled/
sudo nginx -t
```

Jeśli test się powiódł:
```bash
sudo systemctl reload nginx
```

### 9.4. Sprawdź status Nginx

```bash
sudo systemctl status nginx
```

---

## 🔥 Krok 10: Konfiguracja Firewall

### 10.1. Skonfiguruj UFW (Uncomplicated Firewall)

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status
```

---

## ✅ Krok 11: Testowanie

### 11.1. Sprawdź czy aplikacja działa

Otwórz w przeglądarce:
- http://145.239.90.136/

Powinieneś zobaczyć stronę InstalAlarm.

### 11.2. Sprawdź logi

```bash
# Logi Gunicorn
sudo journalctl -u instalalarm -f

# Logi Nginx
sudo tail -f /var/log/nginx/instalalarm_error.log

# Logi Django
tail -f /home/instalalarm/Instalalarm/logs/django.log
```

---

## 🔒 Krok 12: Konfiguracja SSL (Let's Encrypt) - OPCJONALNE

### 12.1. Zainstaluj Certbot

```bash
sudo apt install -y certbot python3-certbot-nginx
```

### 12.2. Uzyskaj certyfikat SSL (tylko jeśli masz domenę)

```bash
sudo certbot --nginx -d instalalarm.pl -d www.instalalarm.pl
```

Certbot automatycznie zaktualizuje konfigurację Nginx.

---

## 🔄 Krok 13: Aktualizacje w przyszłości

### 13.1. Aktualizacja kodu

```bash
cd /home/instalalarm/Instalalarm
source venv/bin/activate
git pull origin main  # lub master
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart instalalarm
```

---

## 🛠️ Rozwiązywanie problemów

### Problem: Błąd 502 Bad Gateway

1. Sprawdź czy Gunicorn działa:
```bash
sudo systemctl status instalalarm
```

2. Sprawdź logi:
```bash
sudo journalctl -u instalalarm -n 50
```

3. Sprawdź czy port 8000 jest otwarty:
```bash
sudo netstat -tlnp | grep 8000
```

### Problem: Statyczne pliki nie ładują się

1. Sprawdź uprawnienia:
```bash
sudo chown -R instalalarm:www-data /home/instalalarm/Instalalarm/staticfiles
sudo chmod -R 755 /home/instalalarm/Instalalarm/staticfiles
```

2. Uruchom ponownie collectstatic:
```bash
source venv/bin/activate
python manage.py collectstatic --noinput
```

### Problem: Błąd bazy danych

1. Sprawdź połączenie:
```bash
sudo -u postgres psql -d instalalarm_db -U instalalarm_user
```

2. Sprawdź DATABASE_URL w .env

### Problem: Błąd 500 Internal Server Error

1. Sprawdź DEBUG=False w .env
2. Sprawdź logi Django:
```bash
tail -f /home/instalalarm/Instalalarm/logs/django.log
```

---

## 📝 Ważne uwagi

1. **Zawsze używaj `source venv/bin/activate`** przed uruchomieniem komend Django
2. **NIGDY nie commituj pliku `.env`** - jest w `.gitignore`
3. **Regularnie twórz kopie zapasowe bazy danych:**
```bash
sudo -u postgres pg_dump instalalarm_db > backup_$(date +%Y%m%d).sql
```
4. **Monitoruj logi regularnie** - sprawdzaj błędy
5. **Aktualizuj system:** `sudo apt update && sudo apt upgrade`

---

## 🎉 Gotowe!

Twoja aplikacja powinna być teraz dostępna pod adresem:
- http://145.239.90.136/
- http://145.239.90.136/admin/ (panel administracyjny)

**Gratulacje! 🎊**

