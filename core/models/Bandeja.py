from django.db import models
from .Usuario import Usuario


class Bandeja(models.Model):
    idBandeja = models.AutoField(
        db_column='id_bandeja',
        primary_key=True
    )
    usuarioEmisor = models.ManyToManyField(
        Usuario,
        db_column='usuario_emisor',
        related_name='USUARIO_EMISOR'
    )
    usuarioReceptor = models.ManyToManyField(
        Usuario,
        db_column='usuario_receptor',
        related_name='USUARIO_RECEPTOR'
    )
    estado = models.BooleanField(
        db_column='estado',
        default=False
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
        db_table = 'MAE_BANDEJA'
