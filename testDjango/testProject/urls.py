from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),    # URL의 path가 'home/'일 경우 일단 home앱으로 가봐라.
    path('', RedirectView.as_view(url='home/', permanent=True)),
]
