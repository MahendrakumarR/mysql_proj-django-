from django.shortcuts import render, redirect
from .forms import MyRegisterForm
from django.contrib import messages            # here using messages for below declaration
from .models import RegisterForm               # import from models.py

def home(request):
    data = RegisterForm.objects.all()         # here collect all data from models.py 
    if(data!=''):
        return render(request,"home.html",{'data':data})
    else:
        return render(request,"home.html")
     

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

def update(request,id):
    data = RegisterForm.objects.get(id=id)     # here get only the id 
    if request.method=='POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']

        data.name = name
        data.age = age
        data.address = address
        data.contact = contact
        data.email = email
        data.save()
        messages.success(request,"Update Successfully Completed")
        return redirect("home")
    return render(request,"update.html", {'data':data})

def delete(request,id):
    data = RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request,"Delete Successfully Completed")
    return redirect('home')
# Create your views here.
