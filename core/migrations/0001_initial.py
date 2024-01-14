# Generated by Django 5.0.1 on 2024-01-13 23:27

import core.models.CustomValidations
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(db_column='id_categoria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', validators=[core.models.CustomValidations.validate_is_string])),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
            ],
            options={
                'db_table': 'MAE_CATEGORIA',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('idDistrito', models.AutoField(db_column='id_distrito', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=100, validators=[core.models.CustomValidations.validate_is_string])),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
            ],
            options={
                'db_table': 'MAE_DISTRITO',
            },
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idTipoUsuario', models.AutoField(db_column='id_tipo_usuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=100, validators=[core.models.CustomValidations.validate_is_string])),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
            ],
            options={
                'db_table': 'MAE_TIPO_USUARIO',
            },
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('idUniversidad', models.AutoField(db_column='id_universidad', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=150, validators=[core.models.CustomValidations.validate_is_string])),
                ('extension', models.CharField(db_column='extension', max_length=100)),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
            ],
            options={
                'db_table': 'MAE_UNIVERSIDAD',
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('idCarrera', models.AutoField(db_column='id_carrera', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', validators=[core.models.CustomValidations.validate_is_string])),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
                ('universidad', models.ForeignKey(db_column='universidad', on_delete=django.db.models.deletion.CASCADE, to='core.universidad')),
            ],
            options={
                'db_table': 'MAE_CARRERA',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(db_column='id_usuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=100, validators=[core.models.CustomValidations.validate_is_string])),
                ('apellido', models.CharField(db_column='apellido', max_length=150, validators=[core.models.CustomValidations.validate_is_string])),
                ('genero', models.BooleanField(db_column='genero')),
                ('fechaNacimiento', models.DateTimeField(db_column='fecha_nacimiento', validators=[core.models.CustomValidations.validate_born_date])),
                ('imagenPerfil', models.ImageField(db_column='imagen_perfil', default='core/img/prefil.png', upload_to='files/img/usuario')),
                ('descripcion', models.TextField(blank=True, db_column='descripcion', null=True)),
                ('puntajeHabito', models.CharField(blank=True, db_column='puntaje_habito', max_length=1, null=True)),
                ('correo', models.EmailField(db_column='correo', max_length=254, unique=True)),
                ('contrasenia', models.CharField(db_column='contrasenia')),
                ('activo', models.BooleanField(db_column='activo', default=False)),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
                ('carrera', models.ForeignKey(db_column='carrera', on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
                ('tipoUsuario', models.ForeignKey(db_column='tipo_usuario', on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario')),
            ],
            options={
                'db_table': 'MAE_USUARIO',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('idEntrada', models.AutoField(db_column='id_entrada', primary_key=True, serialize=False)),
                ('titulo', models.CharField(db_column='titulo', max_length=150)),
                ('prefacio', models.TextField(db_column='prefacio')),
                ('imagen', models.ImageField(db_column='imagen', upload_to='files/img/entrada')),
                ('cuerpo', models.TextField(db_column='cuerpo')),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
                ('categoria', models.ForeignKey(db_column='categoria', on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('usuarioPK', models.ForeignKey(db_column='usuario_pk', on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
            options={
                'db_table': 'MAE_ENTRADA',
            },
        ),
        migrations.CreateModel(
            name='Bandeja',
            fields=[
                ('idBandeja', models.AutoField(db_column='id_bandeja', primary_key=True, serialize=False)),
                ('estado', models.BooleanField(db_column='estado', default=False)),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
                ('usuarioEmisor', models.ManyToManyField(db_column='usuario_emisor', related_name='USUARIO_EMISOR', to='core.usuario')),
                ('usuarioReceptor', models.ManyToManyField(db_column='usuario_receptor', related_name='USUARIO_RECEPTOR', to='core.usuario')),
            ],
            options={
                'db_table': 'MAE_BANDEJA',
            },
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('idVivienda', models.AutoField(db_column='id_vivienda', primary_key=True, serialize=False)),
                ('cantidadHabitacion', models.IntegerField(db_column='cantidad_habitacion')),
                ('cantidadBanio', models.IntegerField(db_column='cantidad_banio')),
                ('estacionamiento', models.IntegerField(db_column='estacionamiento')),
                ('presupuesto', models.IntegerField(db_column='presupuesto')),
                ('usuarioAdicion', models.CharField(blank=True, db_column='usuario_adicion')),
                ('usuarioModificacion', models.CharField(blank=True, db_column='usuario_modificacion', null=True)),
                ('fechaAdicion', models.DateTimeField(auto_now_add=True, db_column='fecha_adicion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column='fecha_modificacion')),
                ('distrito', models.ForeignKey(db_column='distrito', on_delete=django.db.models.deletion.CASCADE, to='core.distrito')),
            ],
            options={
                'db_table': 'MAE_VIVIENDA',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='vivienda',
            field=models.ForeignKey(blank=True, db_column='vivienda', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.vivienda'),
        ),
    ]
