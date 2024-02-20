# Generated by Django 4.2.6 on 2023-10-31 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_rename_file_seller_tb_file_product_tb'),
        ('buyer', '0002_cart_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=20)),
                ('Phonenumber', models.CharField(max_length=20)),
                ('GrandTotal', models.IntegerField()),
                ('Status', models.CharField(default='Pending', max_length=20)),
                ('Buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
            ],
        ),
        migrations.CreateModel(
            name='orderitems_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('Buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
                ('Orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_tb')),
                ('Productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product_tb')),
            ],
        ),
    ]
