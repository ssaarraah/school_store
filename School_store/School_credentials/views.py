from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']
        pw2 = request.POST['password1']
        if pw == pw2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME ALREADY TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pw)

                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not matched.")
            return redirect('register')

        return redirect('/')




    return  render(request, "register.html")
