from django.db import models
from .Universidad import Universidad
from .CustomValidations import *


class Carrera(models.Model):
    idCarrera = models.AutoField(
        db_column='id_carrera',
        primary_key=True
    )
    nombre = models.CharField(
        db_column='nombre',
        validators=[validate_is_string]
    )
    universidad = models.ForeignKey(
        Universidad,
        on_delete=models.CASCADE,
        db_column='universidad',
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
        db_table = 'MAE_CARRERA'
