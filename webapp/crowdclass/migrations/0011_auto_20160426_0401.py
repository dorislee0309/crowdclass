# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdclass', '0010_auto_20160426_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='bardescription',
            name='score',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='bulgedescription',
            name='score',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='dustdescription',
            name='score',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='edgedescription',
            name='score',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='ellipticaldescription',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lensdescription',
            name='score',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='mergingdescription',
            name='score',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='spiraldescription',
            name='score',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='tidaldescription',
            name='score',
            field=models.IntegerField(default=4),
        ),
    ]
