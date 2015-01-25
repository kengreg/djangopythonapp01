# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0020_auto_20141214_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variostelefonos',
            name='persona',
            field=models.ForeignKey(to='publichtml.Persona', null=True),
            preserve_default=True,
        ),
    ]
