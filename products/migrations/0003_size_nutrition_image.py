# Generated by Django 4.0.5 on 2022-06-03 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_drink_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_ml', models.CharField(max_length=45)),
                ('size_fluid_ounce', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'image_urls',
            },
        ),
    ]
