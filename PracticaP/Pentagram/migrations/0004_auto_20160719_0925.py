# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pentagram', '0003_auto_20160718_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pentagram.Photo'),
        ),
    ]
