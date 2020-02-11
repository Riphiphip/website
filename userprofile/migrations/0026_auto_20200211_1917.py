# Generated by Django 3.0.2 on 2020-02-11 19:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0025_remove_profile_tos_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termsofservice',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Publiseringsdato'),
        ),
        migrations.AlterField(
            model_name='termsofservice',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]