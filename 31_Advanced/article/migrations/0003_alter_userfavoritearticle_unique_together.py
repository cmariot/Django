# Generated by Django 5.0.4 on 2024-05-15 08:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userfavoritearticle",
            unique_together={("user", "article")},
        ),
    ]
