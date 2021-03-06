# Generated by Django 2.0.10 on 2019-03-07 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('committees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='main_lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Leder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='committee',
            name='second_lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Nestleder', to=settings.AUTH_USER_MODEL),
        ),
    ]
