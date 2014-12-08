# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0009_auto_20141205_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(null=True, blank=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('M', 'Hombre'), ('F', 'Mujer')], max_length=1),
            preserve_default=True,
        ),
    ]
