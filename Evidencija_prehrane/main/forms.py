from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username","password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class newKorisnikForm(ModelForm):

    first_name = forms.TextInput()
    last_name = forms.TextInput()
    birth_date = forms.DateField()
    email = forms.EmailField()
    phone = forms.TextInput()
    class Meta:
        model = Korisnik
        fields = ['first_name','last_name','birth_date','email','phone']

class newHranaForm(ModelForm):
    
    food_name = forms.TextInput()
    gram_protein = forms.IntegerField()
    gram_fat = forms.IntegerField()
    gram_carbs = forms.IntegerField()

    class Meta:
        model = Hrana
        fields = ['food_name','gram_protein','gram_fat','gram_carbs']
        
class newDesertForm(ModelForm):
    
    desert_name = forms.TextInput()
    choco = forms.Widget()
    kcal = forms.IntegerField()


    class Meta:
        model = Desert
        fields = ['desert_name','choco','kcal']
        
class newEvidencijaForm(ModelForm):
    
	day = forms.TextInput()
	date = forms.DateField()
	user = forms.SelectMultiple()
	meals = forms.SelectMultiple()
	desert_name = forms.Select()
	class Meta:
		model = Evidencija
		fields = ['day','date','user','meals','desert_name']