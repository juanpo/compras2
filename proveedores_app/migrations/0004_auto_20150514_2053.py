# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0003_auto_20150514_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='id',
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='codigo',
            field=models.CharField(max_length=4, serialize=False, primary_key=True),
        ),
    ]
