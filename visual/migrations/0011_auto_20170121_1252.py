# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0019_auto_20170119_1132'),
        ('visual', '0010_auto_20170121_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polygon',
            old_name='children',
            new_name='rect',
        ),
        migrations.RemoveField(
            model_name='polygon',
            name='label',
        ),
        migrations.RemoveField(
            model_name='polygon',
            name='model',
        ),
        migrations.AddField(
            model_name='polygon',
            name='children_placed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='polygon',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='visual.Polygon'),
        ),
        migrations.AddField(
            model_name='polygon',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Topic'),
        ),
    ]