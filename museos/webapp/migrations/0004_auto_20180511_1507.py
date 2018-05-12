# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180511_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 15, 7, 49, 549888, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='seleccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 15, 7, 49, 549263, tzinfo=utc)),
        ),
    ]
