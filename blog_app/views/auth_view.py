from django.shortcuts import render

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
        
        if not email:
            errors['email'] = "Email is required"

        if not password:
            errors['password'] = "Password enter gara"
        
        if not confirm_password:
            errors['confirm_password'] = "Confirm password is required"
        
        if errors:
            return render(request,'auth/register.html',{'error':errors,'prev':request.POST})


    return render(request,'auth/register.html')


def login_method(request):
    return render(request,'auth/login.html')

