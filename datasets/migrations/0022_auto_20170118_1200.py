# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0021_auto_20170118_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='bag_of_words',
            field=models.BinaryField(default=b''),
        ),
    ]
