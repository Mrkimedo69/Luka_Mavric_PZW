from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('korisniks/', include('django.contrib.auth.urls')),
    path('hranas/', include('django.contrib.auth.urls')),
    path('deserts/', include('django.contrib.auth.urls')),
    path('evidencijas/', include('django.contrib.auth.urls')),
]