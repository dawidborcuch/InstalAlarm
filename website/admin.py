from django.contrib import admin
from django.utils.html import format_html
from .models import ZdjecieRealizacji


@admin.register(ZdjecieRealizacji)
class ZdjecieRealizacjiAdmin(admin.ModelAdmin):
    """Admin dla zdjęć realizacji."""
    list_display = ('tytul', 'data_dodania', 'aktywna', 'kolejnosc', 'podglad_zdjecia')
    list_filter = ('aktywna', 'data_dodania')
    search_fields = ('tytul',)
    
    fieldsets = (
        ('Podstawowe informacje', {
            'fields': ('tytul', 'zdjecie', 'aktywna', 'kolejnosc')
        }),
    )
    
    def podglad_zdjecia(self, obj):
        """Wyświetla miniaturkę zdjęcia w liście."""
        if obj.zdjecie:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px; object-fit: cover;" />', obj.zdjecie.url)
        return '-'
    podglad_zdjecia.short_description = 'Podgląd'
