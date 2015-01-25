# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0014_auto_20141214_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variostelefonos',
            name='casa',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
    ]
