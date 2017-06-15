# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okumalar', '0002_auto_20170527_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='okuma',
            name='in_muziki',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='kullanimlari', to='okumalar.Muzik'),
        ),
        migrations.AlterField(
            model_name='okuma',
            name='in_siiri',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='okumalari', to='siirler.Siir'),
        ),
    ]