from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random


# Create your views here.
def home(request):
    #template=loader.get_template('home.html') 
    # return HttpResponse(template.render()).
    return render(request,'home.html')

def password(request):
     
     characters=list('abcdefghijklmnopqrstuvwxyz')

     if request.GET.get('uppercase'):
           characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
     if request.GET.get('special'):
           characters.extend(list('!@#$%^&*()'))      
     if request.GET.get('numbers'):
           characters.extend(list('1234567890'))      

     length = int(request.GET.get('length'))
     thepassword=''
     for x in range(length):
        thepassword +=random.choice(characters)

     return render(request,'password.html', {'password': thepassword})    