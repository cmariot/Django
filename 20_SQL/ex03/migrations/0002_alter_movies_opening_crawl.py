# Generated by Django 5.0.4 on 2024-04-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex03', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='opening_crawl',
            field=models.TextField(blank=True, null=True),
        ),
    ]