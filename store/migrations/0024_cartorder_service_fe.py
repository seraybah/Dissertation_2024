# Generated by Django 3.2.18 on 2023-04-04 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20230403_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='service_fe',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
