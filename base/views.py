from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1,'name':"Learn Python !"},
    {'id':2,'name':"Frontend"},
    {'id':3,'name':"Design Anyone"},
]

# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render(request,'base/home.html',context) 

def room(request,pk):
    return render(request,'base/room.html')
