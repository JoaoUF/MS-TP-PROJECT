from django.db import models
from .Categoria import Categoria
from .Usuario import Usuario


class Entrada(models.Model):
    idEntrada = models.AutoField(
        db_column='id_entrada',
        primary_key=True
    )
    titulo = models.CharField(
        db_column='titulo',
        max_length=150
    )
    prefacio = models.TextField(
        db_column='prefacio'
    )
    imagen = models.ImageField(
        db_column='imagen',
        upload_to='files/img/entrada',
    )
    cuerpo = models.TextField(
        db_column='cuerpo'
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        db_column='categoria'
    )
    usuarioPK = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='usuario_pk'
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
        db_table = 'MAE_ENTRADA'
