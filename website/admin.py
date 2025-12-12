from django.contrib import admin
from .models import Realizacja, ZdjecieRealizacji


class ZdjecieRealizacjiInline(admin.TabularInline):
    """Inline admin dla zdjęć realizacji."""
    model = ZdjecieRealizacji
    extra = 1
    fields = ('zdjecie', 'opis', 'kolejnosc')


@admin.register(Realizacja)
class RealizacjaAdmin(admin.ModelAdmin):
    """Admin dla realizacji."""
    list_display = ('tytul', 'data_dodania', 'aktywna', 'liczba_zdjec')
    list_filter = ('aktywna', 'data_dodania')
    search_fields = ('tytul', 'opis')
    inlines = [ZdjecieRealizacjiInline]
    
    fieldsets = (
        ('Podstawowe informacje', {
            'fields': ('tytul', 'opis', 'aktywna')
        }),
    )
    
    def liczba_zdjec(self, obj):
        """Zwraca liczbę zdjęć dla realizacji."""
        return obj.zdjecia.count()
    liczba_zdjec.short_description = 'Liczba zdjęć'


@admin.register(ZdjecieRealizacji)
class ZdjecieRealizacjiAdmin(admin.ModelAdmin):
    """Admin dla zdjęć realizacji (do zarządzania bezpośrednio)."""
    list_display = ('realizacja', 'opis', 'kolejnosc')
    list_filter = ('realizacja',)
    search_fields = ('realizacja__tytul', 'opis')
