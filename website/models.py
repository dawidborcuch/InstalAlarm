from django.db import models
from django.utils import timezone


class Realizacja(models.Model):
    """Model reprezentujący realizację projektu z możliwością dodania wielu zdjęć."""
    tytul = models.CharField(max_length=200, verbose_name="Tytuł")
    opis = models.TextField(verbose_name="Opis", blank=True)
    data_dodania = models.DateTimeField(default=timezone.now, verbose_name="Data dodania")
    aktywna = models.BooleanField(default=True, verbose_name="Aktywna")
    
    class Meta:
        verbose_name = "Realizacja"
        verbose_name_plural = "Realizacje"
        ordering = ['-data_dodania']
    
    def __str__(self):
        return self.tytul


class ZdjecieRealizacji(models.Model):
    """Model reprezentujący zdjęcie w ramach realizacji."""
    realizacja = models.ForeignKey(Realizacja, on_delete=models.CASCADE, related_name='zdjecia', verbose_name="Realizacja")
    zdjecie = models.ImageField(upload_to='realizacje/', verbose_name="Zdjęcie")
    opis = models.CharField(max_length=200, blank=True, verbose_name="Opis zdjęcia")
    kolejnosc = models.IntegerField(default=0, verbose_name="Kolejność wyświetlania")
    
    class Meta:
        verbose_name = "Zdjęcie realizacji"
        verbose_name_plural = "Zdjęcia realizacji"
        ordering = ['kolejnosc', 'id']
    
    def __str__(self):
        return f"{self.realizacja.tytul} - {self.opis or 'Zdjęcie'}"
