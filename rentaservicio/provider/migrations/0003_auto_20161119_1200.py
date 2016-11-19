# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20161119_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre Especialidad')),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='specialty',
            field=models.ManyToManyField(related_name='especialidades', to='provider.Specialty'),
        ),
    ]