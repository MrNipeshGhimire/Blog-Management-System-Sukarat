from django.shortcuts import render

def login_method(request):
    return render(request,'auth/login.html')

def register_method(request):
    return render(request,'auth/register.html')