# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 30, 16, 18, 16, 890948, tzinfo=utc)),
        ),
    ]
