from django.db import models
from django.utils import timezone


class ZdjecieRealizacji(models.Model):
    """Model reprezentujący zdjęcie realizacji z tytułem."""
    tytul = models.CharField(max_length=200, verbose_name="Tytuł zdjęcia", default="Zdjęcie")
    zdjecie = models.ImageField(upload_to='realizacje/', verbose_name="Zdjęcie")
    data_dodania = models.DateTimeField(default=timezone.now, verbose_name="Data dodania")
    aktywna = models.BooleanField(default=True, verbose_name="Aktywna")
    kolejnosc = models.IntegerField(default=0, verbose_name="Kolejność wyświetlania")
    
    class Meta:
        verbose_name = "Zdjęcie realizacji"
        verbose_name_plural = "Zdjęcia realizacji"
        ordering = ['kolejnosc', '-data_dodania']
    
    def __str__(self):
        return self.tytul


class ContactMessage(models.Model):
    """Model reprezentujący wiadomość z formularza kontaktowego."""
    imie = models.CharField(max_length=100, verbose_name="Imię")
    telefon = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email")
    tresc = models.TextField(verbose_name="Treść wiadomości")
    data_wyslania = models.DateTimeField(default=timezone.now, verbose_name="Data wysłania")
    przeczytane = models.BooleanField(default=False, verbose_name="Przeczytane")
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Adres IP")
    
    class Meta:
        verbose_name = "Wiadomość kontaktowa"
        verbose_name_plural = "Wiadomości kontaktowe"
        ordering = ['-data_wyslania']
    
    def __str__(self):
        return f"{self.imie} - {self.email} ({self.data_wyslania.strftime('%Y-%m-%d %H:%M')})"
