# Generated by Django 3.2.18 on 2023-05-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0037_auto_20230528_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_one',
            name='first',
            field=models.BooleanField(default=False),
        ),
    ]
