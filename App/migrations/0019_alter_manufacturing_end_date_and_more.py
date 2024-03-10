# Generated by Django 4.1.2 on 2024-03-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_alter_manufacturing_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturing',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturing',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='ordered_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
