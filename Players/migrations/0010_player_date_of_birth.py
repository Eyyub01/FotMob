# Generated by Django 5.1.4 on 2024-12-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0009_rename_players_player_alter_player_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]