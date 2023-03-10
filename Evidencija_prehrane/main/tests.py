from django.test import TestCase, Client
from main.models import *
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

class Testmodels(TestCase):

    def setUp(self):
        self.korisnik1 = Korisnik.objects.create(
            first_name = "First Name",
            last_name = "Last Name",
            birth_date = "2022-01-16",
            email = "TestEmail",
            phone = "0912651999",
        )
        self.desert1 = Desert.objects.create(
            desert_name = "desert name",
            choco = "True",
            kcal = "1",
        )
        self.hrana1 = Hrana.objects.create(
            food_name = "food name",
            gram_protein = "5",
            gram_fat = "5",
            gram_carbs = "5"
        )
        self.evidencija1 = Evidencija.objects.create(
            day = "day",
            date = "2022-01-16",
            user = Korisnik.objects.create(first_name = "First Name",
                last_name = "Last Name",
                birth_date = "2022-01-16",
                email = "TestEmail",
                phone = "0912651999"),
            desert_name = Desert.objects.create(
                desert_name = "desert name",
                choco = "True",
                kcal = "1")
        )

    def test_korisnik(self):
        self.assertEquals(self.korisnik1.first_name,"First Name")
    def test_desert(self):
        self.assertEquals(self.desert1.choco,"True")
    def test_hrana(self):
        self.assertEquals(self.hrana1.gram_protein,"5")
    def test_evidencija(self):
        self.assertEquals(self.evidencija1.date,"2022-01-16")
    # def test_evidencija(self):
    #     evidencija1 = Evidencija.objects.create(
    #             day = "day",
    #             date = "2022-01-16",
    #             user = Korisnik.objects.create(first_name = "First Name",
    #                 last_name = "Last Name",
    #                 birth_date = "2022-01-16",
    #                 email = "TestEmail",
    #                 phone = "0912651999"),
    #             desert_name = Desert.objects.create(
    #                 desert_name = "desert name",
    #                 choco = "True",
    #                 kcal = "1")
    #         )
    #     meal1 = Hrana.objects.create(
    #                 food_name = "food name",
    #                 gram_protein = "5",
    #                 gram_fat = "5",
    #                 gram_carbs = "5"),
    #     meal2 = Hrana.objects.create(
    #                 food_name = "food name2",
    #                 gram_protein = "10",
    #                 gram_fat = "10",
    #                 gram_carbs = "10"),
    #     evidencija1.meals.set([meal1.pk,meal2.pk])
    #     self.assertEquals(evidencija1.meals.count(),2)
    
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('main:index')
        self.korisniks_q_url = reverse('main:korisniks')

    def test_project_index_GET(self):
        client = Client()

        response = client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_korisnik_GET(self):
        client = Client()

        response = client.get(self.korisniks_q_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/korisnik_list.html')