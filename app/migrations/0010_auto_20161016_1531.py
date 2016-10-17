# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20161016_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='get_phenotype_weight',
            name='check_point',
            field=models.CharField(default='OUXAN56KC8', max_length=50, unique=True, verbose_name='check_point'),
        ),
        migrations.AlterField(
            model_name='get_genotype',
            name='check_point',
            field=models.CharField(default='FVFFHSMQ6S', max_length=50, unique=True, verbose_name='check_point'),
        ),
        migrations.AlterField(
            model_name='get_phenotype',
            name='check_point',
            field=models.CharField(default='Y15ZUPEFXU', max_length=50, unique=True, verbose_name='check_point'),
        ),
    ]