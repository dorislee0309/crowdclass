# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 03:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdclass', '0006_auto_20160425_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bardescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='bardescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='bulgedescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='bulgedescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='dustdescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='dustdescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='edgedescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='edgedescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='ellipticaldescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='ellipticaldescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='lensdescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='lensdescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='mergingdescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='mergingdescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='spiraldescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='spiraldescription',
            name='score',
        ),
        migrations.RemoveField(
            model_name='tidaldescription',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='tidaldescription',
            name='score',
        ),
    ]
