# Generated by Django 3.2.18 on 2023-04-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0023_basicaddon_payout_vendor_fee_immediately'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='homepage')),
                ('title', models.CharField(default='Keep your new born baby engaged', max_length=1010)),
                ('sub_title', models.CharField(default='Lorem Ipsum is the best way of writing destiny car type', max_length=1010)),
                ('button_text', models.CharField(default='Visit PRoducts', max_length=100)),
                ('button_url', models.URLField(default='https://Desphixs.com/shop/', max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Home Page Setup',
            },
        ),
    ]
