# Generated by Django 2.2 on 2021-06-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(max_length=25),
        ),
    ]
