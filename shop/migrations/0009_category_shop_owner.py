# Generated by Django 4.0.2 on 2022-03-04 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_alter_sales_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='shop_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shop_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
