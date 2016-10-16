# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='do_sack',
            name='sackDate',
        ),
        migrations.RemoveField(
            model_name='do_sack',
            name='sacked',
        ),
        migrations.AddField(
            model_name='do_sack',
            name='corpse',
            field=models.IntegerField(choices=[(0, '丢弃'), (1, '实验'), (2, '送出')], default=0),
        ),
        migrations.AddField(
            model_name='do_sack',
            name='to_mouse',
            field=models.ManyToManyField(related_name='sack', to='app.Mouse', verbose_name='sack mouse event'),
        ),
    ]