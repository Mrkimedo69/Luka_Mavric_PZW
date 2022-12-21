import factory
from factory.django import DjangoModelFactory

from main.models import *
import factory.fuzzy

import random

my_days_list=['Ponedjeljak', 'Utorak',
'Srijeda', 'Četvrtak', 'Petak', 'Subota',
'Nedjelja'
]

class KorisnikFactory(DjangoModelFactory):
	class Meta:
		model = Korisnik

	first_name = factory.Faker("first_name")
	last_name = factory.Faker("last_name")
	birth_date = factory.Faker("date_time")
	email = factory.Faker("free_email")
	phone = factory.Faker("phone_number")

class HranaFactory(DjangoModelFactory):
	class Meta:
		model = Hrana

	food_name=factory.Faker("sentence", nb_words=3)
	gram_protein=factory.fuzzy.FuzzyInteger(5,100)
	gram_fat=factory.fuzzy.FuzzyInteger(5,100)
	gram_carbs=factory.fuzzy.FuzzyInteger(5,100)

class DesertFactory(DjangoModelFactory):
	class Meta:
		model=Desert
	
	desert_name=factory.Faker("sentence", nb_words=2)
	choco=factory.Faker("pybool")
	kcal=factory.fuzzy.FuzzyInteger(100,600)

class EvidencijaFactory(DjangoModelFactory):
	class Meta:
		model=Evidencija
	
	day = factory.Faker("sentence",ext_word_list=my_days_list,nb_words=1)
	date = factory.Faker("date_time")
	user = factory.SubFactory(KorisnikFactory)
	desert_name = factory.Iterator(Desert.objects.all())