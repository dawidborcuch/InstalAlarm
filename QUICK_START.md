# 🚀 Szybki Start - InstalAlarm

## Development (Lokalne środowisko)

### 1. Instalacja

```bash
# Zainstaluj zależności
pip install -r requirements.txt

# (Opcjonalnie) Skonfiguruj .env
cp .env.example .env
# Edytuj .env jeśli potrzebujesz zmienić domyślne wartości
```

### 2. Baza danych

```bash
# Migracje
python manage.py migrate

# Utwórz superużytkownika
python manage.py createsuperuser
```

### 3. Uruchomienie

```bash
# Serwer deweloperski
python manage.py runserver
```

Otwórz: http://127.0.0.1:8000/

---

## 🔄 Workflow

### Commity w development

Możesz normalnie commitować zmiany - **nie wpływają one na produkcję**:

```bash
git add .
git commit -m "Twoja zmiana"
git push
```

### Aktualizacja produkcji

Na serwerze produkcyjnym:

```bash
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart instalalarm
```

---

## 📁 Struktura Settings

- **Development:** `instalalarm.settings.development` (domyślnie w `manage.py`)
- **Production:** `instalalarm.settings.production` (w `wsgi.py`)

**Commity nie psują produkcji** - każdy środowisko ma swoje ustawienia!

---

## ⚙️ Zmienne środowiskowe

Wszystkie wrażliwe dane są w `.env` (nie commituj tego pliku!):

- `SECRET_KEY` - klucz Django
- `DEBUG` - tryb debugowania (True/False)
- `ALLOWED_HOSTS` - dozwolone hosty
- `EMAIL_*` - konfiguracja emaili
- `DATABASE_URL` - URL bazy danych

Szablon: `.env.example`

---

## 📖 Więcej informacji

- **Pełna instrukcja wdrożenia:** [WDROZENIE.md](WDROZENIE.md)
- **Dokumentacja projektu:** [README.md](README.md)

