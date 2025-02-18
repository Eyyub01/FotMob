# Generated by Django 5.1.2 on 2024-12-07 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0006_alter_players_options'),
        ('Teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='players',
            options={'verbose_name': 'Players', 'verbose_name_plural': 'Players'},
        ),
        migrations.AddField(
            model_name='players',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Teams.teams'),
        ),
    ]
