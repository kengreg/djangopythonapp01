# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0016_auto_20141214_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variostelefonos',
            name='casa',
            field=models.CharField(max_length=15, blank=True, null=True, validators=[django.core.validators.RegexValidator(message="T&eacute;lefono debe ser escrito: '+999999999'.", regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=True,
        ),
    ]
