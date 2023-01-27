from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("account:login"))

def createProfile(request):
    info = request.POST
    fname, lname, no, email = info["firstname"], info["lastname"], info["phoneno"], info["email"]
    if fname=="" or lname=="" or no==None or email=="":
        return render(request, "account/login.html", {"error":"Fill all fields correctly"})
    else:
        acc = UserAccount.objects.create(firstName=fname, lastName=lname, phoneNo=int(no), email=email)
        acc.save()
        return HttpResponseRedirect(reverse("account:menu", args=(acc.accountNo,)))

def login(request):
    return render(request, "account/login.html")

def profile(request, accNo):
    pass

def menu(request, accNo):
    return render(request, "account/menu.html")

def transfer(Request, accNo):
    pass

def deposit(Request, accNo):
    pass

def history(request, accNo):
    pass