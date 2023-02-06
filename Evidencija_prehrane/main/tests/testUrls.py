from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('main:index')

        self.assertEquals(resolve(url).func, index)

    def test_korisniks_url_is_resolved(self):
        url = reverse('main:korisniks')

        self.assertEquals(resolve(url).func.view_class, KorisnikList)
    
    def test_hranas_url_is_resolved(self):
        url = reverse('main:hranas')

        self.assertEquals(resolve(url).func.view_class, HranaList)

    def test_deserts_url_is_resolved(self):
        url = reverse('main:deserts')

        self.assertEquals(resolve(url).func.view_class, DesertList)

    def test_evidencijas_url_is_resolved(self):
        url = reverse('main:evidencijas')

        self.assertEquals(resolve(url).func.view_class, EvidencijaList)
        
    def test_register_url_is_resolved(self):
        url = reverse('main:register')

        self.assertEquals(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url = reverse('main:login')

        self.assertEquals(resolve(url).func, login_request)
        
    def test_logout_url_is_resolved(self):
        url = reverse('main:logout')

        self.assertEquals(resolve(url).func, logout_request)

    def test_noviDesert_url_is_resolved(self):
        url = reverse('main:novidesert')

        self.assertEquals(resolve(url).func, newDesert)

    def test_noviKorisnik_url_is_resolved(self):
        url = reverse('main:novikorisnik')

        self.assertEquals(resolve(url).func, newKorisnik)

    def test_novaHrana_url_is_resolved(self):
        url = reverse('main:novahrana')

        self.assertEquals(resolve(url).func, newHrana)

    def test_novaEvidencija_url_is_resolved(self):
        url = reverse('main:novaevidencija')

        self.assertEquals(resolve(url).func, newEvidencija)

