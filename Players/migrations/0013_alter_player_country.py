# Generated by Django 5.1.4 on 2024-12-16 14:12

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0012_player_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
