# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import muebles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0002_auto_20171005_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=240, verbose_name='Descripcion del mueble')),
                ('dimensiones', models.TextField(max_length=240, verbose_name='Dimenciones del mueble')),
                ('foto_1', models.ImageField(max_length=50, upload_to=muebles.models.change_file_name, verbose_name='1ra foto del mueble')),
                ('foto_2', models.ImageField(max_length=50, upload_to=muebles.models.change_file_name, verbose_name='2da foto del mueble')),
                ('foto_3', models.ImageField(max_length=50, upload_to=muebles.models.change_file_name, verbose_name='3ra foto del mueble')),
                ('foto_4', models.ImageField(max_length=50, upload_to=muebles.models.change_file_name, verbose_name='4ta foto del mueble')),
                ('foto_5', models.ImageField(max_length=50, upload_to=muebles.models.change_file_name, verbose_name='5ta foto del mueble')),
                ('modelo', models.CharField(max_length=40, verbose_name='Modelo (Nombre) ')),
                ('oferta', models.SmallIntegerField(default=0, verbose_name='\xbfOferta?')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del mueble')),
                ('slug', models.CharField(blank=True, max_length=140, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categoria')),
            ],
            bases=(muebles.models.SlugMixin, models.Model),
        ),
    ]
