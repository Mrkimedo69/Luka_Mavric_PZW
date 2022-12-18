from django.shortcuts import render
from django.views.generic import ListView
from main.models import Korisnik,Hrana,Desert,Evidencija
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html')

class KorisnikList(ListView):
    model = Korisnik

class HranaList(ListView):
    model = Hrana
    
class DesertList(ListView):
    model = Desert

class EvidencijaList(ListView):
    model = Evidencija

class EvidencijaKorisnikList(ListView):
    template_name = 'main/evidencija_list.html'

    def get_queryset(self):
        self.user = get_object_or_404(Korisnik, first_name=self.kwargs['user'])
        return Evidencija.objects.filter(user=self.user)