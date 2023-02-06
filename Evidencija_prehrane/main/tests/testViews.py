from django.test import TestCase, Client
from django.urls import reverse
from main.models import *

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