from django.shortcuts import render
from django.views.generic import ListView
from main.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

class KorisnikList(ListView):
    model = Korisnik

class HranaList(ListView):
    model = Hrana
    
class DesertList(ListView):
    model = Desert

class EvidencijaList(ListView):
    model = Evidencija

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()

    return render (request=request, template_name="registration/register.html", context={"register":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('main:index')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_request":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:index")


def newKorisnik(request):
	if request.POST:
		form = newKorisnikForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			print(form.instance.id)
		return redirect ("main:index")
	form = newKorisnikForm()
	return render(request, "main/newUser_form.html", {'form':newKorisnikForm})

def newHrana(request):
	if request.POST:
		form = newHranaForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			print(form.instance.id)
		return redirect ("main:index")
	form = newHranaForm()
	return render(request, "main/newHrana_form.html", {'form':newHranaForm})

def newDesert(request):
	if request.POST:
		form = newDesertForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
		return redirect ("main:index")
	form = newDesertForm()
	return render(request, "main/newDesert_form.html", {'form':newDesertForm})

def newEvidencija(request):
	if request.POST:
		form = newEvidencijaForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
		return redirect ("main:index")
	form = newEvidencijaForm()
	return render(request, "main/newEvidencija_form.html", {'form':newEvidencijaForm})	

def korisnik_update(request, id):
        korisnik = Korisnik.objects.get(id=id)
        form = newKorisnikForm(instance=korisnik)
        return render(request,'main/korisnik_update.html',{'form': form})