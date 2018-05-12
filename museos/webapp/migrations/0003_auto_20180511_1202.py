# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180505_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 12, 2, 26, 158459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='seleccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 12, 2, 26, 157850, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
