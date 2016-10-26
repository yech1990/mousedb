# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mouse_born_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouse',
            name='genotype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouse', to='app.Genotype', verbose_name='genotype that this mouse is'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]