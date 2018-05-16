# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180511_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='color',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 15, 9, 56, 39, 413755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='seleccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 15, 9, 56, 39, 413182, tzinfo=utc)),
        ),
    ]
