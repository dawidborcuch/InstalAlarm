# InstalAlarm - Strona Internetowa (Django)

Nowoczesna, responsywna strona internetowa dla firmy InstalAlarm Przemysław Stolarz z panelem administracyjnym Django.

## 🎨 Design

- **Motyw:** Ciemny i elegancki (#1c1c1c)
- **Kolory akcentujące:**
  - Czerwony (#C40000) - przyciski CTA i akcenty
  - Pomarańczowy (#F68C22) - sekcja partnerstwa Eltrox
- **Czcionka:** Poppins (Google Fonts)

## 🚀 Instalacja i Uruchomienie

1. **Zainstaluj zależności:**
```bash
pip install -r requirements.txt
```

2. **Wykonaj migracje bazy danych:**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Utwórz superużytkownika (aby móc logować się do panelu admin):**
```bash
python manage.py createsuperuser
```

4. **Uruchom serwer deweloperski:**
```bash
python manage.py runserver
```

5. **Otwórz w przeglądarce:**
   - Strona główna: http://127.0.0.1:8000/
   - Panel admin: http://127.0.0.1:8000/admin/
   - Realizacje: http://127.0.0.1:8000/realizacje/

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
- Przed wdrożeniem na produkcję zmień `SECRET_KEY` w `settings.py` i ustaw `DEBUG = False`
