# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161014_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouse',
            name='name',
            field=models.CharField(default='?', max_length=50),
        ),
    ]
