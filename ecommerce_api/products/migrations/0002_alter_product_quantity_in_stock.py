# Generated by Django 4.2 on 2023-12-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_in_stock',
            field=models.IntegerField(),
        ),
    ]
