# Generated by Django 4.2.2 on 2023-11-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0046_alter_vendor_address_alter_vendor_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
