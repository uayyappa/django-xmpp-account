# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20160902_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmation',
            name='new_purpose',
            field=models.CharField(choices=[('register', 'registration'), ('password', 'set password'), ('email', 'set email'), ('delete', 'delete')], max_length=12),
        ),
    ]
