"""
Django settings for instalalarm project.

Ten plik jest zachowany dla kompatybilności wstecznej.
Wszystkie ustawienia zostały przeniesione do instalalarm/settings/
- development.py - dla środowiska deweloperskiego
- production.py - dla środowiska produkcyjnego
- base.py - wspólne ustawienia

Dla development użyj: instalalarm.settings.development
Dla production użyj: instalalarm.settings.production
"""

# Importuj ustawienia development jako domyślne (dla kompatybilności)
from .settings.development import *
