# Generated by Django 5.1.4 on 2024-12-16 14:12

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0011_alter_player_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
