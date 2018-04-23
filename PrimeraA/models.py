# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Equipo(models.Model):

    ARICA = 'santiago'
    IQUIQUE = 'iquique'
    ANTOFAGASA = 'antofagasta'
    CALAMA = 'calama'
    SERENA = 'serena'
    COQUIMBO = 'coquimbo'
    VALPARAISO = 'valparaiso'
    VINA_DEL_MAR = 'vinadelmar'
    QUILLOTA = 'quillota'
    CALERA = 'calera'
    SANTIAGO = 'santiago'
    RANCAGUA = 'rancagua'
    CURICO = 'curico'
    TALCA = 'talca'
    CHILLAN = 'chillan'
    CONCEPCION = 'concepcion'
    TALCAHUANO = 'talcahuano'
    LOS_ANGELES = 'losangeles'
    TEMUCO = 'temuco'
    PUERTO_MONTT = 'ptomontt'


    CATEGORIES_CHOICES = (
        (ARICA, 'Santiago'),
        (IQUIQUE, 'Iquique'),
        (ANTOFAGASA, 'Antofagasta'),
        (CALAMA, 'Calama'),
        (SERENA, 'Serena'),
        (COQUIMBO, 'Coquimbo'),
        (VALPARAISO, 'Valparaiso'),
        (VINA_DEL_MAR, 'Vina del mar'),
        (QUILLOTA, 'Quillota'),
        (CALERA, 'Calera'),
        (SANTIAGO, 'Santiago'),
        (RANCAGUA, 'Rancagua'),
        (CURICO, 'Curico'),
        (TALCA, 'Talca'),
        (CHILLAN, 'Chillan'),
        (CONCEPCION, 'Concepcion'),
        (TALCAHUANO, 'Talcahuano'),
        (LOS_ANGELES, 'Los Angeles'),
        (TEMUCO, 'Temuco'),
        (PUERTO_MONTT, 'Puerto Montt'),
    )

    nombre = models.CharField(max_length=100)
    dt = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)