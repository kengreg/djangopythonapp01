# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0021_auto_20141214_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variostelefonos',
            name='persona',
            field=models.ForeignKey(default=0, to='publichtml.Persona'),
            preserve_default=False,
        ),
    ]
