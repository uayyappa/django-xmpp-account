# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 10:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20160902_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddresses',
            name='purpose',
        ),
    ]