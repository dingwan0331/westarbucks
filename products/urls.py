from django.urls import path 
from products.views import *

urlpatterns = [
    path('',ProductsView.as_view()),  # as.view() 는 HTTP메소드와 클래스메소드를 맵핑시켜주는 메소드
]

## GET 10.234.141.411:8000  ## 뒤에는 자원을 어떤걸 사용할건지를 정하며 동사는 사용하지않는다 // 동사 = HTTP메소드가 알려준다