from pydoc       import describe
from unicodedata import category
from django.db   import models
from products.models import *


class HardSpeed(models.Model):
    
    @staticmethod
    def drinks(kwargs):
        kw = kwargs['drinks']
        Drink.objects.create(
            korean_name  = kw['korean_name'], 
            english_name = kw['english_name'],
            description  = kw['description'],
            category_id  = kw['category_id']
        )
        
    @staticmethod
    def sizes(kwargs):
        kw = kwargs['sizes']
        i = 0
        while i <50:
            try:
                Size.objects.get(size_ml = kw['size_ml'])
                Size.objects.create(
                name = kw['name'],
                size_ml = kw['size_ml'],
                size_fluid_ounce = kw['size_fluid_ounce']
            )
                i += 1
            except:
                i += 1

    @staticmethod
    def allergies(kwargs):
        i = 0
        while i<20:
            try:
                Allergy.objects.get(name = kwargs['allergies'][i])
                Allergy.objects.create(name = kwargs['allergies'][i])
                i += 1
            except:
                i += 1
    
    @staticmethod
    def nutritions(kwargs):
        kw = kwargs['nutritions']
        Nutrition.objects.create(
            one_serving_kcal = kw['one_serving_kcal'],
            sodium_mg        = kw['sodium_mg'],
            saturated_fat_g  = kw['saturated_fat_g'],
            sugars_g         = kw['sugars_g'],
            protein_g        = kw['protein_g'],
            caffeine_mg      = kw['caffeine_mg'],
            drink_id         = kwargs['drink_id'],
            size_id          = Size.objects.get(size_ml = kwargs['sizes']['size_ml']).id
        )

    @staticmethod
    def images(kwargs):
        kw = kwargs['images']
        Image.objects.create(
            image_url = kw['image_url'],
            drink_id = kwargs['drink_id']
            )
    
    @staticmethod
    def allergy_drinks(kwargs):
        for i in kwargs['allergies']:
            AllergyDrink.objects.create(
                drink_id = kwargs['drink_id'],
                allergy_id = Allergy.objects.get(name = i).id
            )

class Done(HardSpeed):
    
    @staticmethod
    def start1(kwargs):
        HardSpeed.drinks(kwargs)
        HardSpeed.allergies(kwargs)
        HardSpeed.sizes(kwargs)
        HardSpeed.nutritions(kwargs)
        HardSpeed.allergy_drinks(kwargs)
        return
        


drinks_dict = { 
        'drinks' : {
            'korean_name'      : '롤린 민트 초코 콜드 브루',
            'english_name'     : 'Rollin Mint Choco cold brew',
            'description'      : '스타벅스의 콜드 브루와 은은한 민트 초코 베이스로 누구나 즐길 수 있는 여름 음료.\n손목의 스냅을 춤을 추듯 가볍게 돌려 음료를 섞어서빨대 없이 즐겨 보세요.',
            'category_id'      : Category.objects.get(name = '콜드 브루 커피').id
        } ,
        'drink_id' : 1,
        'sizes' : {
            'name'             : 'Tall(톨)',
            'size_ml'          : '355ml',
            'size_fluid_ounce' : '12 fl oz'
        } ,
        
        'allergies' : ['대두','두유'],
        'nutritions' : {
            'one_serving_kcal' : 210 ,
            'sodium_mg' :  115,
            'saturated_fat_g' : 4.5,
            'sugars_g' : 28,
            'protein_g' : 6,
            'caffeine_mg' : 131 ,
        },
        'images' : {
            'image_url' : '',
        }
}

'''
def easy_speed(*args,class_name):
    for i in range(len(args)):
        class_name.objects.create(name)
        '''
        #   from products.models import *
        #   from products.text_input.text import *
        #   from products.text_input.template import *
        #   EasySpeed.easy(food_categories)
        #   Drink.objects.bulk_create(drinks_dict)
        #   Done.start1(drinks_dict)