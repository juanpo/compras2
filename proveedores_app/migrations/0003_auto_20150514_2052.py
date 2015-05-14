# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0002_auto_20150514_0214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='nombre',
            new_name='descripcion',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='codigo',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
