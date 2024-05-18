from django import forms               # here create new file forms.py for creating tables in easy method
from .models import RegisterForm       # here import from models.py file

class MyRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = ["name", "age", "address", "contact", "email"]