# Folder na logo

Umieść tutaj plik logo firmy InstalAlarm.

## Wymagania:
- **Nazwa pliku:** `logo.png` (lub zmień w szablonach na inną nazwę)
- **Format:** PNG, SVG, JPG (zalecany PNG z przezroczystym tłem)
- **Rozmiar:** Zalecany około 150-200px szerokości (wysokość automatyczna)
- **Tło:** Przezroczyste lub ciemne (dopasowane do motywu strony)

## Jak dodać logo:

1. Umieść plik logo w tym folderze jako `logo.png`
2. Jeśli używasz innej nazwy pliku, zaktualizuj ścieżkę w szablonach:
   - `website/templates/website/index.html` (2 miejsca: header i footer)
   - `website/templates/website/realizacje.html` (2 miejsca: header i footer)
   
   Zmień: `{% static 'website/images/logo.png' %}` na swoją nazwę pliku.

3. Logo będzie automatycznie wyświetlane w headerze i footerze na wszystkich stronach.

## Alternatywnie:
Możesz również użyć logo w formacie SVG dla lepszej jakości na wszystkich rozdzielczościach.

