# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
