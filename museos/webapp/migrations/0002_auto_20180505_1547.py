# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.AddField(
            model_name='museo',
            name='enlace',
            field=models.CharField(max_length=512, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seleccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 5, 15, 46, 33, 866433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 5, 15, 46, 33, 867113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='museo',
            name='accesibilidad',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='museo',
            name='fax',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='museo',
            name='telefono',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.OneToOneField(related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
