# Generated by Django 4.0.5 on 2022-06-06 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_drink_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllergyrDrink',
            new_name='AllergyDrink',
        ),
    ]