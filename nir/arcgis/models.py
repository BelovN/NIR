from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    IAGA = models.CharField(max_length=150, verbose_name='Краткое название')
    lat = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Широта')
    lon = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Долгота')
    mlat = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Магнитная широта')
    mlon = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Магнитная долгота')

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'
