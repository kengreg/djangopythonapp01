# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0018_auto_20141214_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variostelefonos',
            name='casa',
            field=models.CharField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message="Minimo 7 cifras: '+1234567'.", regex='^\\+?1?\\d{7,15}$')], max_length=15),
            preserve_default=True,
        ),
    ]
