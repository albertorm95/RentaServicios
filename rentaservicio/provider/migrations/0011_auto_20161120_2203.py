# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0010_auto_20161120_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerplace',
            name='day',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')], default='l', max_length=10, verbose_name='Dia de la semana'),
        ),
    ]
