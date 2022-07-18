from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return render(request , 'index.html')

def Signup(request):
   return render(request, 'signup.html')

def Login(request):
   return render(request, 'login.html')

