# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(verbose_name='Dirección'),
        ),
    ]