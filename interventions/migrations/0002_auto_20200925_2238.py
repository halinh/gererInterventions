# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-09-25 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interventions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intervention',
            old_name='nom_intervenant',
            new_name='nomIntervenant',
        ),
    ]