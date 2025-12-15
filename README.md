# InstalAlarm - Strona Internetowa (Django)

Nowoczesna, responsywna strona internetowa dla firmy InstalAlarm Przemysław Stolarz z panelem administracyjnym Django.

## 🎨 Design

- **Motyw:** Ciemny i elegancki (#1c1c1c)
- **Kolory akcentujące:**
  - Czerwony (#C40000) - przyciski CTA i akcenty
  - Pomarańczowy (#F68C22) - sekcja partnerstwa Eltrox
- **Czcionka:** Poppins (Google Fonts)

## 🚀 Instalacja i Uruchomienie (Development)

1. **Zainstaluj zależności:**
```bash
pip install -r requirements.txt
```

2. **Skonfiguruj zmienne środowiskowe (opcjonalne):**
```bash
cp .env.example .env
# Edytuj .env i ustaw wartości dla development
```

3. **Wykonaj migracje bazy danych:**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Utwórz superużytkownika (aby móc logować się do panelu admin):**
```bash
python manage.py createsuperuser
```

5. **Uruchom serwer deweloperski:**
```bash
python manage.py runserver
```

6. **Otwórz w przeglądarce:**
   - Strona główna: http://127.0.0.1:8000/
   - Panel admin: http://127.0.0.1:8000/admin/
   - Realizacje: http://127.0.0.1:8000/realizacje/

## 🚀 Wdrożenie na Produkcję

**Szczegółowa instrukcja wdrożenia znajduje się w pliku [WDROZENIE.md](WDROZENIE.md)**

### Szybki start:
1. Skonfiguruj zmienne środowiskowe na serwerze (`.env` lub panel hostingu)
2. Ustaw `DEBUG=False` i `SECRET_KEY` w produkcji
3. Uruchom migracje i `collectstatic`
4. Skonfiguruj Gunicorn + Nginx (szczegóły w WDROZENIE.md)

### Ważne:
- **Commity w środowisku deweloperskim NIE wpływają na produkcję**
- Produkcja używa `instalalarm.settings.production`
- Development używa `instalalarm.settings.development`
- Wszystkie wrażliwe dane są w zmiennych środowiskowych (`.env`)

## ✨ Funkcjonalności

### Strona Główna
- ✅ Stały (fixed) pasek nawigacyjny
- ✅ Logo InstalAlarm z ikonami
- ✅ Menu: Oferta, Realizacje, O nas, Kontakt
- ✅ Przycisk CTA "Zapytaj o wycenę"
- ✅ Sekcja Hero - pełna wysokość viewport
- ✅ Sekcja Partnerstwa Eltrox
- ✅ Sekcja Usługi (3 kafelki)
- ✅ Podgląd realizacji (3 ostatnie)
- ✅ Footer z danymi kontaktowymi

### Strona Realizacje
- ✅ Pełna galeria realizacji z bazy danych
- ✅ Wyświetlanie zdjęć i opisów
- ✅ Responsywny układ grid
- ✅ Miniaturki dodatkowych zdjęć

### Panel Administracyjny Django
- ✅ Zarządzanie realizacjami
- ✅ Dodawanie wielu zdjęć do każdej realizacji
- ✅ Opisy realizacji i zdjęć
- ✅ Kolejność wyświetlania zdjęć
- ✅ Aktywacja/deaktywacja realizacji

## 📁 Struktura projektu

```
Instalalarm/
├── instalalarm/          # Główna konfiguracja Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── website/              # Aplikacja główna
│   ├── models.py        # Modele (Realizacja, ZdjecieRealizacji)
│   ├── admin.py         # Konfiguracja panelu admin
│   ├── views.py         # Widoki
│   ├── urls.py          # URL-e aplikacji
│   ├── templates/       # Szablony HTML
│   │   └── website/
│   │       ├── index.html
│   │       └── realizacje.html
│   └── static/          # Pliki statyczne
│       └── website/
│           ├── css/
│           │   └── style.css
│           └── js/
│               └── main.js
├── media/               # Przesłane zdjęcia (tworzy się automatycznie)
├── manage.py
└── requirements.txt
```

## 🔧 Zarządzanie Realizacjami przez Panel Admin

### Dodawanie nowej realizacji:

1. Zaloguj się do panelu admin: http://127.0.0.1:8000/admin/
2. Kliknij **"Dodaj Realizację"** w sekcji Website
3. Wypełnij:
   - **Tytuł** - nazwa realizacji
   - **Opis** - szczegółowy opis projektu (opcjonalnie)
   - **Aktywna** - zaznacz, aby wyświetlić na stronie
4. W sekcji **"Zdjęcia realizacji"** (na dole formularza):
   - Kliknij **"Dodaj kolejne Zdjęcie realizacji"**
   - Wybierz zdjęcie z dysku
   - Dodaj opis zdjęcia (opcjonalnie)
   - Ustaw kolejność wyświetlania (0 = pierwsze)
5. Kliknij **"Zapisz"**

### Zarządzanie zdjęciami:

- Możesz dodać wiele zdjęć do każdej realizacji
- Pierwsze zdjęcie (kolejność 0) będzie głównym zdjęciem
- Kolejne zdjęcia będą wyświetlane jako miniatury
- Możesz edytować kolejność, opisy i usuwać zdjęcia

## 📱 Responsywność

Strona jest w pełni responsywna i działa na:
- 📱 Urządzeniach mobilnych (320px+)
- 📱 Tabletach (768px+)
- 💻 Desktopach (1200px+)

## 🎯 Wysoki kontrast

Wszystkie teksty mają wysoki kontrast dla lepszej czytelności:
- Tekst główny: biały (#ffffff) na ciemnym tle
- Tekst drugorzędny: jasnoszary (#b0b0b0)
- Akcenty: czerwony i pomarańczowy

## 📝 Uwagi

- Dane kontaktowe w footerze należy zaktualizować na rzeczywiste
- Placeholder dla logo można zastąpić prawdziwym obrazem
- Obraz tła w sekcji Hero można zastąpić prawdziwym zdjęciem/wideo

## 🔐 Bezpieczeństwo

- **NIGDY nie commituj pliku `.env`** - jest w `.gitignore`
- Wszystkie wrażliwe dane (SECRET_KEY, hasła) są w zmiennych środowiskowych
- W produkcji `DEBUG=False` jest wymuszane przez `settings.production`
- Struktura settings oddziela development od production

## 📁 Struktura Settings

Projekt używa struktury settings z oddzielnymi plikami:
- `instalalarm/settings/base.py` - wspólne ustawienia
- `instalalarm/settings/development.py` - ustawienia dla development
- `instalalarm/settings/production.py` - ustawienia dla produkcji

Dzięki temu commity w środowisku deweloperskim nie wpływają na produkcję.
