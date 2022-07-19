from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def Signup(request):
    if request.method == "POST":
        username = request.POST['fullName']
        email = request.POST['email']
        role = request.POST['role']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.role = role

        myuser.save()

        messages.success(request, " Your account has been successfully created")

        return redirect('Login')
    return render(request, 'signup.html')


def Login(request):
    return render(request, 'Login.html')
