# Generated by Django 4.1.2 on 2023-11-18 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_products_rawmaterial_remove_order_customer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]