# Generated by Django 5.0.4 on 2024-04-26 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tips", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="tip",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="tip",
            name="down",
            field=models.ManyToManyField(
                related_name="down", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="tip",
            name="up",
            field=models.ManyToManyField(
                related_name="up", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
