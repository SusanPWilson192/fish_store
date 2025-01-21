# Generated by Django 5.0.3 on 2024-05-02 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0013_delete_deliverydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliverydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('payment_status', models.CharField(max_length=20, null=True)),
                ('purchase_date', models.DateTimeField(auto_now=True, null=True)),
                ('product_status', models.CharField(default='Order Placed', max_length=50, null=True)),
                ('instruction', models.CharField(default='Your Order Has Been Successfully Placed', max_length=50, null=True)),
                ('productdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.fish')),
                ('userdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.register')),
            ],
        ),
    ]
