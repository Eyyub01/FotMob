# Generated by Django 5.1.4 on 2024-12-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0010_player_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Please write in order YEAR-MONTH-DAY', null=True),
        ),
    ]
