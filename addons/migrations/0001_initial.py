# Generated by Django 3.2.7 on 2023-03-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicAddon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('affiliate_commission_percentage', models.IntegerField(default=50, help_text='NOTE: Numbers added here are in percentage (%)')),
                ('currency_sign', models.CharField(default='$', max_length=10)),
                ('currency_abbreviation', models.CharField(default='USD', max_length=10)),
            ],
            options={
                'verbose_name': 'Basic Addons',
                'verbose_name_plural': 'Basic Addons',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(default='logo.jpg', upload_to='')),
                ('website_address', models.CharField(max_length=500)),
                ('footer', models.CharField(max_length=1000)),
                ('facebook', models.CharField(default='https://facebook.com/', max_length=1000)),
                ('instagram', models.CharField(default='https://instagram.com/', max_length=1000)),
                ('twitter', models.CharField(default='https://twitter.com/', max_length=1000)),
                ('linkedin', models.CharField(default='https://linkedin.com/', max_length=1000)),
                ('youtube', models.CharField(default='https://youtube.com/', max_length=1000)),
                ('telegram', models.CharField(default='https://telegram.com/', max_length=1000)),
                ('homepage', models.CharField(choices=[('live', 'Live'), ('maintainance', 'Maintainance'), ('error', 'Error')], default='live', max_length=1000)),
                ('secret_key', models.CharField(blank=True, max_length=1000, null=True)),
                ('public_key', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Company Information',
            },
        ),
    ]
