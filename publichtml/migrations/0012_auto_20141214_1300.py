# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0011_variostelefonos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variostelefonos',
            old_name='home',
            new_name='Casa',
        ),
    ]
