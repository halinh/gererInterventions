# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-09-25 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('nom_intervenant', models.CharField(default='', max_length=70)),
                ('lieu', models.CharField(default='', max_length=70)),
                ('date', models.DateField()),
            ],
        ),
    ]
