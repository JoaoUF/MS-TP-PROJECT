from django.db import models
from .Vivienda import Vivienda
from .Carrera import Carrera
from .TipoUsuario import TipoUsuario
from .CustomValidations import *
from django.contrib.auth.hashers import make_password


class Usuario(models.Model):
    idUsuario = models.AutoField(
        db_column='id_usuario',
        primary_key=True
    )
    nombre = models.CharField(
        db_column='nombre',
        max_length=100,
        blank=True,
        validators=[validate_is_string]
    )
    apellido = models.CharField(
        db_column='apellido',
        max_length=150,
        blank=True,
        validators=[validate_is_string]
    )
    genero = models.BooleanField(
        db_column='genero',
        blank=True,
    )
    fechaNacimiento = models.DateTimeField(
        db_column='fecha_nacimiento',
        blank=True,
        validators=[validate_born_date]
    )
    imagenPerfil = models.ImageField(
        upload_to='files/img/usuario',
        db_column='imagen_perfil',
        blank=True,
        # default='core/img/prefil.png'
    )
    descripcion = models.TextField(
        db_column='descripcion',
        null=True,
        blank=True
    )
    puntajeHabito = models.CharField(
        db_column='puntaje_habito',
        max_length=1,
        null=True,
        blank=True
    )
    correo = models.EmailField(
        unique=True,
        blank=True,
        db_column='correo'
    )
    contrasenia = models.CharField(
        db_column='contrasenia',
        blank=True,
        max_length=128
    )
    activo = models.BooleanField(
        db_column='activo',
        blank=True,
        default=False
    )
    primerIngreso = models.BooleanField(
        db_column='primer_ingreso',
        blank=True,
        default=False
    )
    carrera = models.ForeignKey(
        Carrera,
        db_column='carrera',
        blank=True,
        on_delete=models.CASCADE
    )
    tipoUsuario = models.ForeignKey(
        TipoUsuario,
        db_column='tipo_usuario',
        blank=True,
        on_delete=models.CASCADE
    )
    vivienda = models.ForeignKey(
        Vivienda,
        db_column='vivienda',
        on_delete=models.CASCADE,
        null=True,
        blank=True
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

    # @property
    # def get_imagenPerfil(self) -> str:
    #     if self.imagenPerfil and hasattr(self.imagenPerfil,'url'):
    #         return f'http://localhost:8000{self.imagenPerfil}'

    class Meta:
        db_table = 'MAE_USUARIO'

    # def save(self, *args, **kwargs):
    #     self.contrasenia = make_password(self.contrasenia)
    #     super(Usuario, self).save(*args, **kwargs)
