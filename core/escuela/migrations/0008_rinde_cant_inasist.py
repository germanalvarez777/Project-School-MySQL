# Generated by Django 4.0.2 on 2022-06-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0007_alter_tiene_hora_egreso_alter_tiene_hora_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='rinde',
            name='cant_inasist',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cant Inasistencias'),
        ),
    ]