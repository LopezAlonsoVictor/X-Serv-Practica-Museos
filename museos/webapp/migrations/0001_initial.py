# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 4, 30, 15, 35, 58, 398297, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=32)),
                ('direccion', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('barrio', models.CharField(max_length=32)),
                ('distrito', models.CharField(max_length=32)),
                ('accesibilidad', models.IntegerField()),
                ('telefono', models.BigIntegerField()),
                ('fax', models.BigIntegerField()),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('museo', models.ForeignKey(to='webapp.Museo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=16)),
                ('color', models.CharField(max_length=16)),
                ('tamaño', models.IntegerField()),
                ('fondo', models.CharField(max_length=16)),
                ('titulo', models.CharField(max_length=16)),
                ('nombre', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='seleccion',
            name='usuario',
            field=models.ForeignKey(to='webapp.Usuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(to='webapp.Museo'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(to='webapp.Usuario'),
        ),
    ]
