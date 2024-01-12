from django.db import models
from .Distrito import Distrito
from .CustomValidations import *


class Vivienda(models.Model):
    idVivienda = models.AutoField(
        db_column='id_vivienda',
        primary_key=True
    )
    cantidadHabitacion = models.IntegerField(
        db_column='cantidad_habitacion',
    )
    cantidadBanio = models.IntegerField(
        db_column='cantidad_banio',
    )
    estacionamiento = models.IntegerField(
        db_column='estacionamiento'
    )
    presupuesto = models.IntegerField(
        db_column='presupuesto'
    )
    distrito = models.ForeignKey(
        Distrito,
        on_delete=models.CASCADE,
        db_column='distrito',
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
