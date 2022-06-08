import json                           # 프론트에서 받은 JSON객체를 파이썬 언어로 사용하기 위해

from django.http import JsonResponse  # 우리가 작성한것들을 JSON형태로 변환하기위해
from django.views import View         # 뷰 클래스 상속을 위

from products.models import *


class ProductsView(View):                # 어떤 자원을 활용해서 할것인가가 클래스명
    def post(self, request):       # HTTP 메소드와 함수이름을 일치시킨다.request 변수는 프론트가 주는 request의 모든 정보가 들어있다. 두개는 필수인자다.
        data     = json.loads(request.body)     # json.loads 는 JSON객체를 파이썬 타입으로 바꿔주는 함수이다. 
        menu     = Menu.objects.create(name=data['menu'])  # 위에서 뽑아온 데이터에서 뽑아서 create // 키는 프론트에서 주는것이다.
        category = Category.objects.create(
            name = data['category']
            menu = menu         # menu_id가 아니라 menu 객체 자체를 넣는다.
        )
        Product.objects.create(
            name     = data['product'], 
            category = category
        )
        return JsonResponse({'messasge':'created'}, status=201)
           # JsonResponse 객체의 첫인자는 response의 바디 status 순으로 인자가 들어간다.

    def get(self, request):
        products = Product.objects.all()
        results  = []

        for product in products:
           results.append(
               {
                   "menu" : product.category.menu.name,
                   "category" : product.category.name,
                   "product_name" : product.name
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)