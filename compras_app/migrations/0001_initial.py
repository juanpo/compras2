# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(default=0)),
                ('orden', models.ForeignKey(to='compras_app.Orden')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('productos', models.ManyToManyField(to='compras_app.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='proveedor',
            field=models.ForeignKey(to='compras_app.Proveedor'),
        ),
    ]
