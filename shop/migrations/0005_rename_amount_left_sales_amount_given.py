# Generated by Django 4.0.2 on 2022-03-02 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='amount_left',
            new_name='amount_given',
        ),
    ]
