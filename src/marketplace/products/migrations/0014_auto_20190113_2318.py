# Generated by Django 2.1.5 on 2019-01-13 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]