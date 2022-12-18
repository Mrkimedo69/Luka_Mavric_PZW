from django.contrib import admin
from main.models import *
# Register your models here.

model_list = [Korisnik,Hrana,Desert,Evidencija]
admin.site.register(model_list)