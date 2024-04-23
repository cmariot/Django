# Generated by Django 5.0.4 on 2024-04-23 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('birth_year', models.CharField(max_length=32, null=True)),
                ('gender', models.CharField(max_length=32, null=True)),
                ('eye_color', models.CharField(max_length=32, null=True)),
                ('hair_color', models.CharField(max_length=32, null=True)),
                ('height', models.IntegerField(null=True)),
                ('mass', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('climate', models.CharField(max_length=64, null=True)),
                ('diameter', models.IntegerField(null=True)),
                ('orbital_period', models.IntegerField(null=True)),
                ('population', models.BigIntegerField(null=True)),
                ('rotation_period', models.IntegerField(null=True)),
                ('surface_water', models.FloatField(null=True)),
                ('terrain', models.CharField(max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('title', models.CharField(max_length=64, unique=True)),
                ('episode_nb', models.IntegerField(primary_key=True, serialize=False)),
                ('opening_crawl', models.TextField(blank=True, null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
                ('characters', models.ManyToManyField(related_name='film', to='ex10.people')),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ex10.planets'),
        ),
    ]
