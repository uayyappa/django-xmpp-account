# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 10:12
from __future__ import unicode_literals

from django.db import migrations


def migrate_purpose(apps, schema_editor):
    Confirmation = apps.get_model('core', 'Confirmation')

    # we don't use constants here because they will be switched in the future
    Confirmation.objects.filter(purpose=0).update(new_purpose='register')
    Confirmation.objects.filter(purpose=1).update(new_purpose='password')
    Confirmation.objects.filter(purpose=2).update(new_purpose='email')
    Confirmation.objects.filter(purpose=3).update(new_purpose='delete')

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_confirmation_new_purpose'),
    ]

    operations = [
        migrations.RunPython(migrate_purpose),
    ]