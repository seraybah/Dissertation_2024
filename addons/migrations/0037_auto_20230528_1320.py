# Generated by Django 3.2.18 on 2023-05-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0036_auto_20230528_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_one',
            name='button_text',
            field=models.CharField(default='Shop Now', max_length=100),
        ),
        migrations.AlterField(
            model_name='home_one',
            name='small_title',
            field=models.CharField(default='Hey there, Welcome!', max_length=1010),
        ),
        migrations.AlterField(
            model_name='home_two',
            name='button_text',
            field=models.CharField(default='Shop Now', max_length=100),
        ),
        migrations.AlterField(
            model_name='home_two',
            name='small_title',
            field=models.CharField(default='Hey there, Welcome!', max_length=1010),
        ),
    ]
