# Generated by Django 5.1.3 on 2024-12-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0003_alter_teams_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='club_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
