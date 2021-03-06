# Generated by Django 4.0.2 on 2022-02-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='especialidad',
            field=models.CharField(max_length=30, verbose_name='La especialidad'),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='estado',
            field=models.CharField(max_length=30, verbose_name='El estado'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='adress',
            field=models.CharField(max_length=200, verbose_name='la direccion'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='sucursal',
            field=models.CharField(max_length=200, verbose_name='la sucursal'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='apellido',
            field=models.CharField(max_length=200, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad.especialidad', verbose_name='La especialidad'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='estado',
            field=models.CharField(max_length=200, verbose_name='El estado'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefone',
            field=models.IntegerField(verbose_name='Teléfono'),
        ),
    ]
