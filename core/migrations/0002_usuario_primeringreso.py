# Generated by Django 5.0.1 on 2024-01-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='primerIngreso',
            field=models.BooleanField(db_column='primer_ingreso', default=False),
        ),
    ]