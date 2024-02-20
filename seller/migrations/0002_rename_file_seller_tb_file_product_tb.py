# Generated by Django 4.2.6 on 2023-10-26 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0002_category_tb'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_tb',
            old_name='file',
            new_name='File',
        ),
        migrations.CreateModel(
            name='product_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('File', models.FileField(upload_to='')),
                ('Price', models.IntegerField()),
                ('Stock', models.IntegerField()),
                ('Details', models.CharField(max_length=20)),
                ('Categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.category_tb')),
                ('Sellerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller_tb')),
            ],
        ),
    ]
