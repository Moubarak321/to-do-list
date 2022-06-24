
from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    # path("testo", views.testo, name="testo")
    path("moub", views.moub, name="moub")
]