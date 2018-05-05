# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180430_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='enlace',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seleccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 17, 12, 48, 672488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 17, 12, 48, 673127, tzinfo=utc)),
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
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='usuario'),
        ),
    ]
