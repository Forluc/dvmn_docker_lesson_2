# Generated by Django 3.2.15 on 2023-10-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0040_auto_20231022_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burgercount',
            name='product',
        ),
        migrations.AddField(
            model_name='burgercount',
            name='product',
            field=models.ManyToManyField(related_name='products', to='foodcartapp.Product', verbose_name='Товар'),
        ),
    ]
