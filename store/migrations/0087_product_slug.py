# Generated by Django 3.2.18 on 2023-05-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0086_alter_product_product_condition_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
