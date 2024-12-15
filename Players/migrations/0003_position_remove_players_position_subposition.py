# Generated by Django 5.1.2 on 2024-12-07 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0002_players_delete_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='players',
            name='position',
        ),
        migrations.CreateModel(
            name='SubPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subpositions', to='Players.position')),
            ],
        ),
    ]
