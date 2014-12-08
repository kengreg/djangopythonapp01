# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0002_auto_20141130_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.PositiveSmallIntegerField(),
            preserve_default=True,
        ),
    ]
