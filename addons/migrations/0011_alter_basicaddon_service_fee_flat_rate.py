# Generated by Django 3.2.18 on 2023-04-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0010_auto_20230411_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicaddon',
            name='service_fee_flat_rate',
            field=models.DecimalField(decimal_places=2, default=0.7, help_text='NOTE: Add the amount you want to charge as service fee e.g $2.30', max_digits=12),
        ),
    ]
