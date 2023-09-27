from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Product,Category

def index(request):
    p = Category.objects.all()
    return render(request,'index.html', {'A':p})

def prod(request,category_id):
    p = Product.objects.filter(category_id=category_id)
    return render(request, 'p0.html', {'A': p})

def display_image(request,id):
    p = Product.objects.get(id=id)
    return render(request, 'p1.html', {'product': p})

def account(request):
    return render(request,'account.html')

def cart(request,):
     return render(request,'cart.html')

