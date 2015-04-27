# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras_app', '0003_remove_proveedor_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='orden',
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
    ]
