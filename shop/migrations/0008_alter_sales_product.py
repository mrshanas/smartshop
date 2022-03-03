# Generated by Django 4.0.2 on 2022-03-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_quantity_alter_sales_quantity_bought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold', to='shop.product'),
        ),
    ]
