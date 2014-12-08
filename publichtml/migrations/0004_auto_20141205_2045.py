# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0003_auto_20141130_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
            preserve_default=True,
        ),
    ]
