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
