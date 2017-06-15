# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siirler', '0008_auto_20170527_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitap',
            options={'get_latest_by': 'in_basim_senesi', 'ordering': ['-in_yazari'], 'verbose_name': 'Kitap', 'verbose_name_plural': 'KİTAPLAR'},
        ),
        migrations.AlterModelOptions(
            name='sair',
            options={'ordering': ['in_adi'], 'verbose_name': 'ŞAİR', 'verbose_name_plural': 'ŞAİRLER'},
        ),
        migrations.AlterModelOptions(
            name='siir',
            options={'ordering': ['in_sairi'], 'verbose_name': 'ŞİİR', 'verbose_name_plural': 'ŞİİRLER'},
        ),
    ]