# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdclass', '0004_auto_20160425_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='bardescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bulgedescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='dustdescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='edgedescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ellipticaldescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='lensdescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='mergingdescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='spiraldescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='tidaldescription',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
