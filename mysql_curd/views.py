from django.shortcuts import render
from .forms import MyRegisterForm

def home(request):
    return render(request, "home.html")

def insert(request):
    form = MyRegisterForm()
    return render(request, "register.html", {'form':form})
# Create your views here.
