from django.db import models
from .CustomValidations import *


class Distrito(models.Model):
    idDistrito = models.AutoField(
        db_column='id_distrito',
        primary_key=True
    )
    nombre = models.CharField(
        db_column='nombre',
        max_length=100,
        validators=[validate_is_string]
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
        db_table = 'MAE_DISTRITO'
