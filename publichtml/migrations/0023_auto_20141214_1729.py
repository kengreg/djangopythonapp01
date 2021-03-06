# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0022_auto_20141214_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variostelefonos',
            name='casa',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{7,15}$', message="Minimo 7 cifras: '+1234567'.")], max_length=15, blank=True, default=1),
            preserve_default=False,
        ),
    ]
