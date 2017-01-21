# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0012_auto_20170121_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polygon',
            name='rect',
        ),
        migrations.AddField(
            model_name='polygon',
            name='rect_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polygon',
            name='rect_left',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polygon',
            name='rect_top',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polygon',
            name='rect_width',
            field=models.IntegerField(default=0),
        ),
    ]