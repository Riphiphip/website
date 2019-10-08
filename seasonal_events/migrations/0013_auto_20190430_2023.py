# Generated by Django 2.0.10 on 2019-04-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasonal_events', '0012_auto_20190430_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='logo',
            field=models.ImageField(blank=True, help_text='Dersom ingen logo lastes opp brukes standard hackerspace-logo', null=True, upload_to='seasonal_events/logos/'),
        ),
        migrations.AlterField(
            model_name='season',
            name='manual_override',
            field=models.BooleanField(help_text='Tving sesongen til å være aktiv', verbose_name='Manuel overskriving'),
        ),
    ]