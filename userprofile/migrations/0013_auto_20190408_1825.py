# Generated by Django 2.0.13 on 2019-04-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_auto_20190408_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_discord',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Discord-tag'),
        ),
    ]
