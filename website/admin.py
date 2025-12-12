from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe
from datetime import timedelta
from .models import ZdjecieRealizacji, ContactMessage


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


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin dla wiadomości kontaktowych."""
    list_display = ('imie', 'email', 'telefon', 'data_wyslania', 'przeczytane', 'akcje')
    list_filter = ('przeczytane', 'data_wyslania')
    search_fields = ('imie', 'email', 'telefon', 'tresc')
    readonly_fields = ('imie', 'telefon', 'email', 'tresc', 'data_wyslania', 'ip_address')
    date_hierarchy = 'data_wyslania'
    
    fieldsets = (
        ('Informacje kontaktowe', {
            'fields': ('imie', 'telefon', 'email', 'ip_address')
        }),
        ('Wiadomość', {
            'fields': ('tresc',)
        }),
        ('Status', {
            'fields': ('przeczytane', 'data_wyslania')
        }),
    )
    
    def akcje(self, obj):
        """Przycisk do oznaczania jako przeczytane."""
        if not obj.przeczytane:
            url = reverse('admin:website_contactmessage_mark_read', args=[obj.pk])
            return format_html('<a class="button" href="{}">Oznacz jako przeczytane</a>', url)
        return '-'
    akcje.short_description = 'Akcje'
    
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/mark-read/', self.mark_as_read, name='website_contactmessage_mark_read'),
        ]
        return custom_urls + urls
    
    def mark_as_read(self, request, pk):
        """Oznacz wiadomość jako przeczytaną."""
        message = ContactMessage.objects.get(pk=pk)
        message.przeczytane = True
        message.save()
        from django.contrib import messages
        messages.success(request, 'Wiadomość oznaczona jako przeczytana.')
        from django.shortcuts import redirect
        return redirect('admin:website_contactmessage_changelist')
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        
        # Statystyki
        total_messages = ContactMessage.objects.count()
        unread_messages = ContactMessage.objects.filter(przeczytane=False).count()
        today_messages = ContactMessage.objects.filter(data_wyslania__date=timezone.now().date()).count()
        week_messages = ContactMessage.objects.filter(data_wyslania__gte=timezone.now() - timedelta(days=7)).count()
        
        extra_context['stats'] = {
            'total': total_messages,
            'unread': unread_messages,
            'today': today_messages,
            'week': week_messages,
        }
        
        return super().changelist_view(request, extra_context=extra_context)
