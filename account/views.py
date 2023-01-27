from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("account:login"))

def login(request):
    return render(request, "account/login.html")

def profile(request, accNo):
    pass

def menu(request, accNo):
    pass

def transfer(Request, accNo):
    pass

def history(request, accNo):
    pass