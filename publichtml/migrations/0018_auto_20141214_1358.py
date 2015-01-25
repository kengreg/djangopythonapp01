# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0017_auto_20141214_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variostelefonos',
            name='casa',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Telefono debe ser escrito: '+999999999'.", regex='^\\+?1?\\d{9,15}$')], blank=True),
            preserve_default=True,
        ),
    ]
