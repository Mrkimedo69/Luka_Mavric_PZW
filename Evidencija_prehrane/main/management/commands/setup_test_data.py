import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Korisnik,Hrana,Desert,Evidencija
from main.factory import (
    KorisnikFactory,
    HranaFactroy,
    DesertFactory,
    EvidencijaFactory
)

NUM_KORISNIK = 5
NUM_HRANA = 5
NUM_DESERT = 10
NUM_EVIDENCIJA = 5


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Korisnik,Hrana,Desert,Evidencija]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KORISNIK):
            korisnik = KorisnikFactory()

        for _ in range(NUM_HRANA):
            hrana = HranaFactroy()
            
        for _ in range(NUM_DESERT):
            desert = DesertFactory()

        for _ in range(NUM_EVIDENCIJA):
            evidencija = EvidencijaFactory()
