# Generated by Django 3.2.18 on 2023-05-06 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0077_auto_20230506_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitem',
            name='saved',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Amount saved by customer', max_digits=12, null=True),
        ),
    ]
