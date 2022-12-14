# Generated by Django 4.0.6 on 2022-08-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='modified_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('physical', 'physical'), ('digital', 'digital')], max_length=15),
        ),
    ]
