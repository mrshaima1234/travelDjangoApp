from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['mail']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(username=user_name, password=password, first_name=fname,
                                                last_name=lname,
                                                email=email)
                user.save()
        else:
            messages.info(request, "password not matching")
            return redirect("register")
        print('user created')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        getusername = request.POST['username']
        getpassword = request.POST['password']
        user = auth.authenticate(username=getusername, password=getpassword)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credential")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
