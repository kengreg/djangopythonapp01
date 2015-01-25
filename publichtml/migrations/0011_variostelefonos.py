# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('publichtml', '0010_auto_20141205_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variostelefonos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('home', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('work', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('other', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('numeropersona', models.ForeignKey(to='publichtml.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
