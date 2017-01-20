# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0031_dataset_error_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermInDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Dataset')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Document')),
            ],
        ),
        migrations.AddField(
            model_name='term',
            name='documents_indexed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='termindocument',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Term'),
        ),
    ]
