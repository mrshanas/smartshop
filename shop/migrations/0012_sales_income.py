# Generated by Django 4.0.3 on 2022-03-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_sales_shop_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='income',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=9),
            preserve_default=False,
        ),
    ]
