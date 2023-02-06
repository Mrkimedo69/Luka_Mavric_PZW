from django.urls import path
from . import views
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('korisniks/', KorisnikList.as_view(), name="korisniks"),
    path('hranas/', HranaList.as_view(), name="hranas"),
    path('deserts/', DesertList.as_view(), name="deserts"),
    path('evidencijas/', EvidencijaList.as_view(), name="evidencijas"),
    path('register/',views.register, name='register'),
    path('login/',views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
    path("novidesert/",views.newDesert, name="novidesert"),
    path("novikorisnik/",views.newKorisnik, name="novikorisnik"),
    path("novahrana/",views.newHrana, name="novahrana"),
    path("novaevidencija/",views.newEvidencija, name="novaevidencija"),   
    # path("updatekorisnik/",views.korisnik_update, name="updatekorisnik"),   
]