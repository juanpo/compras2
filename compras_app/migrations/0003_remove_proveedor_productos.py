# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras_app', '0002_auto_20150420_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='productos',
        ),
    ]
