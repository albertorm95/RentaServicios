# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20161119_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprovider',
            name='providerplace',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='provider.ProviderPlace', verbose_name='Relacion Proveedor-Lugar'),
        ),
    ]
