# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siirler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sair',
            name='slug',
            field=models.SlugField(blank=True, help_text='A label for URL config.', max_length=31, unique=True),
        ),
    ]
