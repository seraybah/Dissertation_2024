# Generated by Django 3.2.18 on 2023-04-19 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0060_auto_20230418_2200'),
        ('vendor', '0024_notification_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productbidders'),
        ),
        migrations.AddField(
            model_name='notification',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productoffers'),
        ),
    ]
