# Generated by Django 4.0.2 on 2022-02-24 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0002_alter_cita_estado_alter_cita_fecha_alter_cita_medico_and_more'),
        ('resultado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='cita',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consulta.cita', verbose_name='Cita'),
        ),
        migrations.AlterField(
            model_name='examen',
            name='costo',
            field=models.IntegerField(verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='examen',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='examen',
            name='estado',
            field=models.CharField(max_length=200, verbose_name='Estado'),
        ),
    ]