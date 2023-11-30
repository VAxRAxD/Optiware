# Generated by Django 4.1.2 on 2023-11-30 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_alter_customer_contact_alter_customer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('ordered_date', models.DateField(blank=True, null=True)),
                ('received_date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('purchase_status', models.CharField(choices=[('Ordered', 'Ordered'), ('Acquired', 'Acquired')], default='Ordered', max_length=200, null=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.supplier')),
            ],
        ),
    ]
