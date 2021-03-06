# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdclass', '0005_auto_20160425_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='bar_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='bulge_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='dust_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='edge_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='elliptical_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='lens_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='merging_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='spiral_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='tidal_description',
            field=models.BooleanField(default=False),
        ),
    ]
