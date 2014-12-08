# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0008_auto_20141205_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.PositiveSmallIntegerField(default=3),
            preserve_default=False,
        ),
    ]
