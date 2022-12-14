# Generated by Django 4.0.6 on 2022-07-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateField()),
                ('modified_at', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('product_type', models.CharField(choices=[('P', 'physical'), ('D', 'digital')], max_length=1)),
            ],
        ),
    ]
