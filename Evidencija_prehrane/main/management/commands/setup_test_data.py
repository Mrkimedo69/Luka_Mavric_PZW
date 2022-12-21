import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Korisnik,Hrana,Desert,Evidencija
from main.factory import (
    KorisnikFactory,
    HranaFactory,
    DesertFactory,
    EvidencijaFactory
)

NUM_KORISNIK = 5
NUM_HRANA = 3
NUM_DESERT = 5
NUM_EVIDENCIJA = 2
FOOD_PER_USER = 5


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Korisnik,Hrana,Desert,Evidencija]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        food = []
        for _ in range(NUM_HRANA):
            meal = HranaFactory()
            food.append(meal)

        for _ in range(NUM_KORISNIK):
            korisnik = KorisnikFactory()

        for _ in range(NUM_HRANA):
            hrana = HranaFactory()
            
        for _ in range(NUM_DESERT):
            desert = DesertFactory()

        for _ in range(NUM_EVIDENCIJA):
            evidencija = EvidencijaFactory()
            meals = random.choices(food,k=FOOD_PER_USER)
            evidencija.meals.add(*meals)
