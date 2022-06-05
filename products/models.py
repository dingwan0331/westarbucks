from pydoc       import describe
from unicodedata import category
from django.db   import models

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    name         = models.CharField(max_length=45)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name  = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description  = models.TextField()

    class Meta:
        db_table = 'drinks'

class AllergyrDrink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drink'

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'allergies'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
    sodium_mg        = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
    saturated_fat_g  = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
    sugars_g         = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
    protein_g        = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
    caffeine_mg      = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
    size             = models.ForeignKey('Size',on_delete=models.CASCADE , null = True)
    drink            = models.ForeignKey('Drink', on_delete=models.CASCADE , null = True)
    
    class Meta:
        db_table = 'nutritions'

class Size(models.Model):
    name             = models.CharField(max_length=45)
    size_ml          = models.CharField(max_length=45 , blank = True)
    size_fluid_ounce = models.CharField(max_length=45 , blank = True)

    class Meta:
        db_table = 'sizes'

class Image(models.Model):
    drink     = models.ForeignKey('Drink',on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2000)
    
    class Meta:
        db_table = 'image_urls'