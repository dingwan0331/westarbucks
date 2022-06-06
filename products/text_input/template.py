from pydoc                    import describe
from unicodedata import category
from django.db                import models
from products.models          import *

           
class HardSpeed(models.Model):
    
    @staticmethod
    def drinks(kwargs):
        kw = kwargs['drinks']
        Drink.objects.update_or_create(
            korean_name  = kw['korean_name'], 
            english_name = kw['english_name'],
            description  = kw['description'],
            category_id  = kw['category_id']
        )
        
    @staticmethod
    def sizes(kwargs):
        kw = kwargs['sizes']
        Size.objects.get_or_create(
                name = kw['name'],
                size_ml = kw['size_ml'],
                size_fluid_ounce = kw['size_fluid_ounce']
                )
        

    @staticmethod
    def allergies(kwargs):
        for i in kwargs['allergies']:
            Allergy.objects.get_or_create(name = i)

    
    @staticmethod
    def nutritions(kwargs):
        kw = kwargs['nutritions']
        Nutrition.objects.update_or_create(
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
        Image.objects.update_or_create(
            image_url = kw['image_url'],
            drink_id = kwargs['drink_id']
            )
    
    @staticmethod
    def allergy_drinks(kwargs):
        for i in kwargs['allergies']:
            AllergyDrink.objects.get_or_create(
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
        HardSpeed.images(kwargs)
        return

drinks_dict = { 
        'drinks' : {
            'korean_name'      : '나이트로 바닐라 크림',
            'english_name'     : 'Nitro Vanilla Cream',
            'description'      : '부드러운 목넘김의 나이트로 커피와 바닐라 크림의 매력을 한번에 느껴보세요!',
            'category_id'      : Category.objects.get(name = '콜드 브루 커피').id
        } ,
        'drink_id' : 2,
        'sizes' : {
            'name'             : 'Tall(톨)',
            'size_ml'          : '355ml',
            'size_fluid_ounce' : '12 fl oz'
        } ,
        
        'allergies' : ['우유'],
        'nutritions' : {
            'one_serving_kcal' : 80 ,
            'sodium_mg' :  40,
            'saturated_fat_g' : 2,
            'sugars_g' : 10,
            'protein_g' : 1,
            'caffeine_mg' : 232,
        },
        'images' : {
            'image_url' : 
            'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000002487]_20210426091745609.jpg',
        }
}
        
drinks_dict1 = { 
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
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2022/04/[9200000003988]_20220406113215431.jpg',
        }
}


drinks_dict2 = { 
        'drinks' : {
            'korean_name'      : '오늘의 커피',
            'english_name'     : 'Brewed Coffee',
            'description'      : '시즌에 어울리는 하나의 원두 종류를 선정하여 신선하게 브루드(Brewed)되어 제공되는 드립커피로 원두 커피의 풍부한 맛과 향을 따뜻하게 즐기실 수 있습니다.',
            'category_id'      : Category.objects.get(name = '브루드 커피').id
        } ,
        'drink_id' : 3,
        'sizes' : {
            'name'             : 'Tall(톨)',
            'size_ml'          : '355ml',
            'size_fluid_ounce' : '12 fl oz'
        } ,
        
        'allergies' : [],
        'nutritions' : {
            'one_serving_kcal' : 5 ,
            'sodium_mg' :  10,
            'saturated_fat_g' : None,
            'sugars_g' : None,
            'protein_g' : None,
            'caffeine_mg' : 260 ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[2]_20210430111934246.jpg',
        }
}
#######################
americano = { 
        'drinks' : {
            'korean_name'      : '아이스 카페 아메리카노',
            'english_name'     : 'Iced Caffe Americano',
            'description'      : '풍부하고 진한 농도의 에스프레소에 시원한 정수물을 더하여 스타벅스의 깔끔하고 강렬한 에스프레소를 부드럽지만 시원하게 즐기실 수 있는 커피입니다.',
            'category_id'      : Category.objects.get(name = '에스프레소').id
        } ,
        'drink_id' : 4,
        'sizes' : {
            'name'             : 'Tall(톨)',
            'size_ml'          : '355ml',
            'size_fluid_ounce' : '12 fl oz'
        } ,
        
        'allergies' : [],
        'nutritions' : {
            'one_serving_kcal' : 10 ,
            'sodium_mg' :  5,
            'saturated_fat_g' : None,
            'sugars_g' : None,
            'protein_g' : 1,
            'caffeine_mg' : 150 ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[110563]_20210426095937947.jpg',
        }
}

rumshot = { 
        'drinks' : {
            'korean_name'      : '럼 샷 코르타도',
            'english_name'     : 'Rum Shot Cortado',
            'description'      : '[더종로R, 청담스타R 전용음료] 최고의 리저브 에스프레소 샷, 스팀 밀크 그리고 럼이 짙게 어우러진 스타벅스 리저브 만의 코르타도입니다.',
            'category_id'      : Category.objects.get(name = '에스프레소').id
        } ,
        'drink_id' : 5,
        'sizes' : {
            'name'             : 'Short(숏)',
            'size_ml'          : '237ml',
            'size_fluid_ounce' : '8 fl oz'
        } ,
        
        'allergies' : ['우유'],
        'nutritions' : {
            'one_serving_kcal' : 70 ,
            'sodium_mg' :  45,
            'saturated_fat_g' : 1.8,
            'sugars_g' : 8,
            'protein_g' : 3,
            'caffeine_mg' : 160 ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/02/[9200000001086]_20210225090838935.jpg',
        }
}

javachip = { 
        'drinks' : {
            'korean_name'      : '자바 칩 프라푸치노',
            'english_name'     : 'Java Chip Frappuccino',
            'description'      : "'나만의 프라푸치노'로 변경되어 우유 선택과 커피 농도 조절이 가능한 블렌디드 음료입니다. 초콜릿 모카 시럽 그리고 진한 초콜릿 칩이 입안에 느껴지는 스타벅스에서만 맛보실 수 있는 신개념 음료로 시원한 커피와 함께 초콜릿 칩의 씹히는 맛이 이색적입니다.",
            'category_id'      : Category.objects.get(name = '프라푸치노').id
        } ,
        'drink_id' : 6,
        'sizes' : {
            'name'             : 'Tall(톨)',
            'size_ml'          : '355ml',
            'size_fluid_ounce' : '12 fl oz'
        } ,
        
        'allergies' : ['대두','우유','밀'],
        'nutritions' : {
            'one_serving_kcal' : 340 ,
            'sodium_mg' :  180,
            'saturated_fat_g' : 9,
            'sugars_g' : 42,
            'protein_g' : 6,
            'caffeine_mg' : 100 ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[168016]_20210415154152277.jpg',
        }
}

jeju = { 
        'drinks' : {
            'korean_name'      : '제주 쑥떡 크림 프라푸치노',
            'english_name'     : 'Jeju Mugwort Cream Frappuccino',
            'description'      : '[제주지역 한정음료] 제주 쑥쑥 라떼의 시원한 버전으로\n쫄깃쫄깃한 국내산 흑임자 떡으로 씹는 재미를 즐길 수 있는 음료.',
            'category_id'      : Category.objects.get(name = '프라푸치노').id
        } ,
        'drink_id' : 7,
        'sizes' : {
            'name'             : 'Grande(그란데)',
            'size_ml'          : '473ml',
            'size_fluid_ounce' : '16 fl oz'
        } ,
        
        'allergies' : ['대두','우유','밀'],
        'nutritions' : {
            'one_serving_kcal' : 460 ,
            'sodium_mg' :  250,
            'saturated_fat_g' : 10,
            'sugars_g' : 57,
            'protein_g' : 8,
            'caffeine_mg' : None ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2022/03/[9200000002090]_20220329144733515.jpg',
        }
 }
##############
twist = { 
        'drinks' : {
            'korean_name'      : '트위스트 피치 요거트 블렌디드',
            'english_name'     : 'Twist Peach Yogurt Blended',
            'description'      : '에버랜드의 대표적인 스릴 어트렉션인 렛츠 트위스트에서 영감을 받은 에버랜드에서만 즐길 수 있는 에버랜드 특화 음료.상큼 달콤한 복숭아와 요거트가 트위스트된 과일 블렌디드.',
            'category_id'      : Category.objects.get(name = '블랜디드').id
        } ,
        'drink_id' : 8,
        'sizes' : {
            'name'             : 'Grande(그란데)',
            'size_ml'          : '473ml',
            'size_fluid_ounce' : '16 fl oz'
        } ,
        
        'allergies' : ['대두','우유','복숭아'],
        'nutritions' : {
            'one_serving_kcal' : 390 ,
            'sodium_mg' :  65,
            'saturated_fat_g' : 1.2,
            'sugars_g' : 68,
            'protein_g' : 3,
            'caffeine_mg' : None ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2022/02/[9200000003987]_20220215170842199.jpg',
        }
 }

passion = { 
        'drinks' : {
            'korean_name'      : '패션 탱고 티 레모네이드 피지오',
            'english_name'     : 'Passion Tango Tea Lemonade Starbucks Fizzio™',
            'description'      : '상큼함이 특징인 패션 티를 진하게 우린 후 상큼한 레모네이드를 더한 뒤, 스타벅스 만의 전용 머신을 이용해 스파클링한, 청량감 있는 음료입니다. 꽃 향기와 달콤하고 상큼한 시트러스 향을 탄산과 함께 더욱 풍부하게 느끼고 싶으시다면 패션 티 레모네이드 피지오를 선택해 보세요! 언제 찾아도 기분이 좋아지는 훌륭한 음료입니다.\n\n※스타벅스 피지오란?\n\n스타벅스만의 독점 기술로 완성한 고급 피지오 머신을 이용하여 바리스타가 한 잔씩 직접 만들어 제공되는 수제 프리미엄 스파클링 음료입니다.',
            'category_id'      : Category.objects.get(name = '스타벅스 피지오').id
        } ,
        'drink_id' : 9,
        'sizes' : {
            'name'             : 'Tall(톨)',
            'size_ml'          : '355ml',
            'size_fluid_ounce' : '12 fl oz'
        } ,
        
        'allergies' : [],
        'nutritions' : {
            'one_serving_kcal' : 65 ,
            'sodium_mg' :  0.2,
            'saturated_fat_g' : None,
            'sugars_g' : 17,
            'protein_g' : None,
            'caffeine_mg' : None ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[107031]_20210419125350068.jpg',
        }
 }

earlgrey = { 
        'drinks' : {
            'korean_name'      : '허니 얼 그레이 밀크 티',
            'english_name'     : 'Honey Earl Grey Milk Tea',
            'description'      : '베르가못 향 가득한 진한 티바나 얼 그레이 티에\n꿀이 더해져 달콤하고 부드러운 밀크 티',
            'category_id'      : Category.objects.get(name = '티(티바나)').id
        } ,
        'drink_id' : 10,
        'sizes' : {
            'name'             : 'Grande(그란데)',
            'size_ml'          : '473ml',
            'size_fluid_ounce' : '16 fl oz'
        } ,
        
        'allergies' : ['우유'],
        'nutritions' : {
            'one_serving_kcal' : 395 ,
            'sodium_mg' :  210,
            'saturated_fat_g' : 8,
            'sugars_g' : 45,
            'protein_g' : 12,
            'caffeine_mg' : 70 ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2020/09/[9200000003233]_20200911143800291.jpg',
        }
 }

jeju_black = { 
        'drinks' : {
            'korean_name'      : '제주 까망 라떼',
            'english_name'     : 'Jeju Black Sesame Latte',
            'description'      : '[제주지역 한정음료] 제주도의 돌담길과 하르방의 풍경을 느낄 수 있는 음료로 고소한 흑임자와 달콤한 소보로 토핑으로 누구나 즐길 수 있는 음료',
            'category_id'      : Category.objects.get(name = '기타 제조 음료').id
        } ,
        'drink_id' : 11,
        'sizes' : {
            'name'             : 'Grande(그란데)',
            'size_ml'          : '473ml',
            'size_fluid_ounce' : '16 fl oz'
        } ,
        
        'allergies' : ['땅콩','대두','우유','난류','밀','오징어'],
        'nutritions' : {
            'one_serving_kcal' : 445 ,
            'sodium_mg' :  250,
            'saturated_fat_g' : 7,
            'sugars_g' : 49,
            'protein_g' : 13,
            'caffeine_mg' : None ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2020/09/[9200000001301]_20200921171639786.jpg',
        }
 }

star_ruby = { 
        'drinks' : {
            'korean_name'      : '스타 루비 자몽 스위트 591ML',
            'english_name'     : 'Star Ruby Grapefruit Sweet 591ML',
            'description'      : '리프레시가 필요할 땐!\n상큼 달콤한 자몽으로 채우기\n과즙이 풍부하고 당도가 높은 스타 루비 자몽이 가득 들어간 상큼한 음료',
            'category_id'      : Category.objects.get(name = '스타벅스 주스 (병음료)').id
        } ,
        'drink_id' : 12,
        'sizes' : {
            'name'             : '',
            'size_ml'          : '473ml',
            'size_fluid_ounce' : ''
        } ,
        
        'allergies' : [],
        'nutritions' : {
            'one_serving_kcal' : 406 ,
            'sodium_mg' :  10,
            'saturated_fat_g' : None,
            'sugars_g' : 100,
            'protein_g' : 0.6,
            'caffeine_mg' : None ,
        },
        'images' : {
            'image_url' : 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/10/[9300000003774]_20211020095032676.jpg',
        }
 }

        #   from products.models import *
        #   from products.text_input.text import *
        #   from products.text_input.template import *
        #   EasySpeed.easy(food_categories)
        #   Drink.objects.bulk_create(drinks_dict)
        #   Done.start1(drinks_dict)