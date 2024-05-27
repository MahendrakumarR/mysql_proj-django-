from django.shortcuts import render, redirect
from .forms import MyRegisterForm
from django.contrib import messages            # here using messages for below declaration

def home(request):
    return render(request, "home.html")

def insert(request):
    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Registration Successfully Completed")
                return redirect("home")        # Here using home name from urls.py
            except:
                pass
    else:
        form = MyRegisterForm()
    return render(request, "register.html", {'form':form})
# Create your views here.
