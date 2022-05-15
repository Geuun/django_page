from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.hello, name='hello'), # testProject/urls.py 를 한 번 거쳐서 온 요청의 URL의 path가 빈 문자열일 경우 home/view.py 안의 hello 함수의 규칙을 따라라.
    
]