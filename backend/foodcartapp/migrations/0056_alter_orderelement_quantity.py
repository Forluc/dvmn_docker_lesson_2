# Generated by Django 3.2.15 on 2023-12-25 18:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0055_order_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderelement',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Количество'),
        ),
    ]
