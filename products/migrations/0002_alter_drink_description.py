# Generated by Django 4.0.5 on 2022-06-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]