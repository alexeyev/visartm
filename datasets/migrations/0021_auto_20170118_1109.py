# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0020_auto_20170118_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='bag_ow_words',
            new_name='bag_of_words',
        ),
    ]