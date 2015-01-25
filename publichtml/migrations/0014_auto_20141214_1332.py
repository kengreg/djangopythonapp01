# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0013_auto_20141214_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variostelefonos',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='variostelefonos',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='variostelefonos',
            name='otro',
        ),
        migrations.RemoveField(
            model_name='variostelefonos',
            name='trabajo',
        ),
        migrations.AlterField(
            model_name='variostelefonos',
            name='casa',
            field=models.CharField(blank=True, max_length=15),
            preserve_default=True,
        ),
    ]
