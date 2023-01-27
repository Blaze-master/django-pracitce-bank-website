from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("login/", views.login, name="login"),
    path("login-error/", views.submitLogin, name="submit-login"),
    path("create-profile/", views.createProfile, name="create-profile"),
    path("creation-error/", views.create, name="create"),
    path("accNo/profile/", views.profile, name="profile"),
    path("accNo/menu/", views.menu, name="menu"),
    path("accNo/transfer/", views.transfer, name="transfer"),
    path("accNo/deposit/", views.deposit, name="deposit"),
    path("accNo/history/", views.history, name="history"),
    path("<accNo>/", views.menu, name="menu"),
]