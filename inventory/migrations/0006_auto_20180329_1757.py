# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-29 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20180329_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='borrower',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
