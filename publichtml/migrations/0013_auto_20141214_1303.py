# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0012_auto_20141214_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variostelefonos',
            old_name='Casa',
            new_name='casa',
        ),
        migrations.RenameField(
            model_name='variostelefonos',
            old_name='fax_number',
            new_name='celular',
        ),
        migrations.RenameField(
            model_name='variostelefonos',
            old_name='mobile',
            new_name='fax',
        ),
        migrations.RenameField(
            model_name='variostelefonos',
            old_name='other',
            new_name='otro',
        ),
        migrations.RenameField(
            model_name='variostelefonos',
            old_name='work',
            new_name='trabajo',
        ),
    ]
