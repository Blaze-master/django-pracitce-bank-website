from django.urls import path
from . import views

urlpatterns = [
    path("accNo/", views.menu, name=""),
    path("login/", views.login, name="login"),
    path("createProfile/", views.createProfile, name="createProfile"),
    path("", views.index, name=""),
    path("accNo/profile/", views.profile, name="profile"),
    path("accNo/menu/", views.menu, name="menu"),
    path("accNo/transfer/", views.transfer, name="transfer"),
    path("accNo/deposit/", views.deposit, name="deposit"),
    path("accNo/history/", views.history, name="history"),
]