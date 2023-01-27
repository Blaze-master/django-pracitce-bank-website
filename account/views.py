from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("account:login"))

def create(request):
    info = request.POST
    fname, lname, no, email, passwd = info["firstname"], info["lastname"], info["phoneno"], info["email"], info["password"]
    if fname=="" or lname=="" or no==None or email=="" or passwd=="":
        return render(request, "account/create.html", {"error":"Fill all fields correctly"})
    else:
        acc = UserAccount.objects.create(firstName=fname, lastName=lname, phoneNo=int(no), email=email, password=passwd)
        acc.save()
        return HttpResponseRedirect(reverse("account:menu", args=(acc.accountNo,)))

def createProfile(request, error=None):
    return render(request, "account/create.html", {"error":error})

def login(request, error=None):
    context = {"error" : error}
    return render(request, "account/login.html", context)

def profile(request, accNo):
    pass

def submitLogin(request):
    accNo = None
    found = False
    for acc in UserAccount.objects.all():
        print(request.POST["accountNo"], acc.accountNo)
        print(request.POST["password"], acc.password)
        if int(request.POST["accountNo"]) == acc.accountNo and request.POST["password"] == acc.password:
            accNo = acc.accountNo
            found = True
            break
    if found:
        print("correct")
        return HttpResponseRedirect(reverse("account:menu", args=(accNo,)))
    else:
        error = "Incorrect username or password"
        return render(request, "account/login.html", {"error":error})

def menu(request, accNo):
    account = UserAccount.objects.get(pk=accNo)
    return render(request, "account/menu.html", {"account":account})


def transfer(Request, accNo):
    pass

def deposit(Request, accNo):
    pass

def history(request, accNo):
    pass