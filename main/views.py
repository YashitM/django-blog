from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hi This is my first Project in Django. </h1>")

def timer(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return HttpResponse("Current Time = "+ current_time)