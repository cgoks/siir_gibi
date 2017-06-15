# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siirler', '0007_auto_20170527_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitap',
            options={'get_latest_by': 'in_basim_senesi', 'ordering': ['-in_yazari'], 'verbose_name': 'Kitap Bilgisi'},
        ),
        migrations.AlterModelOptions(
            name='sair',
            options={'ordering': ['in_adi'], 'verbose_name': 'ŞAİR'},
        ),
        migrations.AlterModelOptions(
            name='siir',
            options={'ordering': ['in_sairi'], 'verbose_name': 'ŞİİR'},
        ),
        migrations.AlterField(
            model_name='kitap',
            name='in_basim_senesi',
            field=models.IntegerField(blank=True),
        ),
    ]
