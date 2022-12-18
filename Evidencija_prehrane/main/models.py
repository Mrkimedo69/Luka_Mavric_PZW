from django.db import models

class Hrana(models.Model):

    food_name = models.CharField("Naziv hrane",max_length=20, null=True)
    gram_protein = models.CharField("Grama proteina",max_length=3,null=True)
    gram_fat = models.CharField("Grama masnoce",max_length=3,null=True)
    gram_carbs = models.CharField("Grama ugljikohidrata",max_length=3,null=True)

    def __str__(self):
        return self.food_name

class Desert(models.Model):

    desert_name = models.CharField("Naziv deserta",max_length=20,null=True)
    choco = models.BooleanField("Cokoladno",default=True,null=True)
    kcal = models.CharField("Kalorije",max_length=3,null=True)

    def __str__(self):
        return self.desert_name

class Korisnik(models.Model):

    first_name = models.CharField("Ime", max_length=64, null=True)
    last_name = models.CharField("Prezime", max_length=64, null=True)
    birth_date = models.DateField("Datum rođenja", blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    phone = models.CharField("Telefon", max_length=15, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Evidencija(models.Model):

    day = models.CharField("Dan",max_length=20, null=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey("Korisnik",verbose_name="Korisnik",on_delete=models.CASCADE,null=True, blank=True)
    meals = models.ManyToManyField(Hrana)
    desert_name = models.OneToOneField(Desert, on_delete = models.CASCADE,default = None, blank=True, null=True)
