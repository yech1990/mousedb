# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20161016_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get_genotype',
            name='check_point',
            field=models.CharField(default='2K33APIA04', max_length=50, unique=True, verbose_name='check_point'),
        ),
        migrations.AlterField(
            model_name='get_phenotype',
            name='check_point',
            field=models.CharField(default='SQ2U6LCGMS', max_length=50, unique=True, verbose_name='check_point'),
        ),
        migrations.AlterField(
            model_name='get_phenotype_weight',
            name='check_point',
            field=models.CharField(max_length=50, unique=True, verbose_name='check_point'),
        ),
    ]