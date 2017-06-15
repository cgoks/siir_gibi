# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siirler', '0010_auto_20170527_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siir',
            name='in_kitabi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kitaptaki_siirleri', to='siirler.Kitap'),
        ),
        migrations.AlterField(
            model_name='siir',
            name='in_tarihi',
            field=models.IntegerField(blank=True, null=True, verbose_name='siirin_tarihi'),
        ),
    ]