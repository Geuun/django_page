from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

# http://localhost
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),    # URL의 path가 'home/'일 경우 일단 home앱으로 가봐라.
    path('', RedirectView.as_view(url='home/', permanent=True)),    #path에 공백을 넣게되면 자동으로 /home 으로 리다이렉트 되는 코드 따라서 http://127.0.0.1:8000/ 을 입력하더라도 http://127.0.0.1:8000/home/으로 이동시킨다.
    
]
