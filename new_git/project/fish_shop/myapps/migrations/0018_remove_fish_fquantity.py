# Generated by Django 5.0.3 on 2024-05-10 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0017_alter_deliverydetails_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='fquantity',
        ),
    ]
