# Generated by Django 4.1.2 on 2023-11-18 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_customer_order_rawmaterials_transaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('thickness', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('thickness', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RemoveField(
            model_name='rawmaterials',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sender',
        ),
        migrations.AddField(
            model_name='supplier',
            name='contact',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='RawMaterials',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.supplier'),
        ),
        migrations.AddField(
            model_name='products',
            name='raw_material',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.rawmaterial'),
        ),
    ]
