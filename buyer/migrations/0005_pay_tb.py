# Generated by Django 4.2.6 on 2023-11-01 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_order_tb_orderdate_order_tb_ordertime'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('CardNumber', models.CharField(max_length=20)),
                ('CVV', models.CharField(max_length=20)),
                ('Exp_Date', models.CharField(max_length=20)),
                ('Buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
                ('Orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_tb')),
            ],
        ),
    ]
