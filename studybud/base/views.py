from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#create a view
def home(request):
    #Return a basic respone
    return HttpResponse('Home page')

def room(request):
    return HttpResponse('ROOM')