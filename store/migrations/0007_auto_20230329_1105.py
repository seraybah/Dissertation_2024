# Generated by Django 3.2.18 on 2023-03-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20230329_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
