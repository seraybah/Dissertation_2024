# Generated by Django 3.2.18 on 2023-04-02 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20230402_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='buyer_shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer_address', to='store.address'),
        ),
    ]
