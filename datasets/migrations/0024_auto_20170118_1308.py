# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0023_auto_20170118_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='word_json_provided',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dataset',
            name='word_uci_provided',
            field=models.BooleanField(default=False),
        ),
    ]
