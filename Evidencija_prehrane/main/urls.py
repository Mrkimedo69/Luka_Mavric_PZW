from django.urls import path
from . import views
from main.views import KorisnikList,HranaList,DesertList,EvidencijaList,EvidencijaKorisnikList

urlpatterns = [
    path('', views.index, name='index.html'),
    path('korisniks/', KorisnikList.as_view()),
    path('hranas/', HranaList.as_view()),
    path('deserts/', DesertList.as_view()),
    path('evidencijas/', EvidencijaList.as_view()),
    path('<user>', EvidencijaKorisnikList.as_view())
]