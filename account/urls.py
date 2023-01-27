from django.urls import path
from . import views

urlpatterns = [
    path("accNo/", views.menu, name=""),
    path("login/", views.login, name="login"),
    path("accNo/profile/", views.profile, name="profile"),
    path("accNo/transfer/", views.transfer, name="transfer"),
    path("accNo/history/", views.history, name="history"),
]