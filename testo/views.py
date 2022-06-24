from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "testo/index.html")

def moub(request):
    return HttpResponse("Hello guys!!!")