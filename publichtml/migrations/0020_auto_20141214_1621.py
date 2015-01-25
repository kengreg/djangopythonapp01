# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0019_auto_20141214_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variostelefonos',
            old_name='numeropersona',
            new_name='persona',
        ),
    ]
