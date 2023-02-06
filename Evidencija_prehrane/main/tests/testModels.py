from django.test import TestCase
from main.models import *

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
    