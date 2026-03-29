from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def register_method(request):
    errors = {}
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # validation
        if not username:
            errors['username'] = "Username is required"
        if User.objects.filter(username=username).exists():
            errors['username'] = "Username already exists"

        
        if not email:
            errors['email'] = "Email is required"
        elif User.objects.filter(email=email).exists():
            errors['email'] = "Email already exists !! use another"

        if not password:
            errors['password'] = "Password enter gara"
        
        if not confirm_password:
            errors['confirm_password'] = "Confirm password is required"
        
        if password != confirm_password:
            errors['confirm_password'] = "Confirm password is not matched !!"
        
        if errors:
            return render(request,'auth/register.html',{'error':errors,'prev':request.POST})
        else:
            user = User.objects.create_user(
                username=username,
                email= email,
                password=password
            )
            user.save()
            messages.success(request,"User registered successfully")
            return redirect('login')
            
    return render(request,'auth/register.html')


def login_method(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

       # validation 
        if not username:
           errors['username'] = "Username is required"
        elif not User.objects.filter(username=username).exists():
            errors['username'] = "Username does not exists"

        if not password:
           errors['password'] = "Password is required"
        
        if errors:
           return render(request,'auth/login.html',{'error':errors,'data':request.POST})
        else:
            # if there is not any errors
            # authenticate() => username and password check graxa 
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)  # session generate garxa 
                messages.success(request,"User logged in successfully !! ")
                return redirect('index')
            else:
                messages.error(request,'Incorrect Password')
                return redirect('login')
                
    return render(request,'auth/login.html')


def logout_method(request):
    logout(request)
    messages.success(request,'Logout Successfully !!')
    return redirect('index')


