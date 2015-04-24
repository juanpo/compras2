# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='orden',
            field=models.ForeignKey(to='compras_app.Orden', null=True),
        ),
    ]
