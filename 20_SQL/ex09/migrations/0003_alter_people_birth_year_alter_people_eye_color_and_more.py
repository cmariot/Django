# Generated by Django 5.0.4 on 2024-04-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0002_alter_people_homeworld_alter_planets_climate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='birth_year',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='mass',
            field=models.FloatField(null=True),
        ),
    ]
