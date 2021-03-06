# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-16 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoorStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Door Statuses',
            },
        ),
        migrations.CreateModel(
            name='OpenData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened', models.DateTimeField()),
                ('closed', models.DateTimeField()),
            ],
        ),
    ]
