# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0006_auto_20141205_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')]),
            preserve_default=True,
        ),
    ]
