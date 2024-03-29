# Generated by Django 5.0.1 on 2024-03-06 19:38

import core.models.CustomValidations
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='activo',
            field=models.BooleanField(blank=True, db_column='activo', default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(blank=True, db_column='apellido', max_length=150, validators=[core.models.CustomValidations.validate_is_string]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='carrera',
            field=models.ForeignKey(blank=True, db_column='carrera', on_delete=django.db.models.deletion.CASCADE, to='core.carrera'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contrasenia',
            field=models.CharField(blank=True, db_column='contrasenia', max_length=128),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(blank=True, db_column='correo', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fechaNacimiento',
            field=models.DateTimeField(blank=True, db_column='fecha_nacimiento', validators=[core.models.CustomValidations.validate_born_date]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.BooleanField(blank=True, db_column='genero'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagenPerfil',
            field=models.ImageField(blank=True, db_column='imagen_perfil', upload_to='files/img/usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(blank=True, db_column='nombre', max_length=100, validators=[core.models.CustomValidations.validate_is_string]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='primerIngreso',
            field=models.BooleanField(blank=True, db_column='primer_ingreso', default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.ForeignKey(blank=True, db_column='tipo_usuario', on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario'),
        ),
    ]
