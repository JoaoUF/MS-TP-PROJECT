from django.db import models
from .CustomValidations import *


class Vivienda(models.Model):
    idVivienda = models.AutoField(
        db_column='id_vivienda',
        primary_key=True
    )
    latitud = models.FloatField(
        db_column='latitud',
    )
    longitud = models.FloatField(
        db_column='longitud'
    )
    radio = models.IntegerField(
        db_column='radio'
    )
    usuarioAdicion = models.CharField(
        db_column='usuario_adicion',
        blank=True
    )
    usuarioModificacion = models.CharField(
        db_column='usuario_modificacion',
        null=True,
        blank=True
    )
    fechaAdicion = models.DateTimeField(
        auto_now_add=True,
        db_column='fecha_adicion',
        editable=False
    )
    fechaModificacion = models.DateTimeField(
        auto_now=True,
        db_column='fecha_modificacion',
    )

    class Meta:
        db_table = 'MAE_VIVIENDA'
