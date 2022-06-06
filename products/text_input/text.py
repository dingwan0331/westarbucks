from products.models import *
from django.db       import models


menus                   = ['음료' , '푸드' , '상품' , '카드' , '메뉴 이야기']
dirnk_categories        = ['콜드 브루 커피','브루드 커피' , '에스프레소' , '프라푸치노' , '블랜디드' , '스타벅스 피지오' , '티(티바나)' , '기타 제조 음료' , '스타벅스 주스 (병음료)']
food_categories         = ['브레드' , '케이크' , '샌드위치 & 샐러드' , '따뜻한 푸드' , '과일 & 요거트' , '스낵 & 미니 디저트' , '아이스크림']
item_categories         = ['머그', '글라스' , '플라스틱 터블러' , '스테인레스 텀블러' , '보온병' , '액세서리' , '선물세트' , '커피 용품']
card_categories         = ['실물카드' , 'e-Gift 카드']
menu_story_categories   = ['나이트로 콜드브루' , '콜드 브루' , '스타벅스 티바나']
kor_cold_brew_coffee    = ['롤린 민트 초코 콜드 블루' , '나이트로 바닐라 크림' , '나이트로 콜드 브루' , '돌체 콜드 브루' , '바닐라 크림 콜드 브루' , '벨벳 다크 모카 나이트로']
eng_cold_brew_coffee    = ['Rollin Mint Choco Cold Brew', ]

class EasySpeed(models.Model):

    @staticmethod
    def easy(class_name,menu__id,args):
        for i in range(len(args)):
            class_name.objects.create(name = args[i] , menu_id = menu__id)
    @staticmethod
    def easy_menus(class_name,args):
        for i in range(len(args)):
            class_name.objects.create(name = args[i])
