from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pneumovis/home.html')

def adddata(request):
    return render(request, 'pneumovis/adddata.html')

def datacards(request):
    return render(request, 'pneumovis/datacards.html')

def help(request):
    return render(request, 'pneumovis/help.html')

def about(request):
    return render(request, 'pneumovis/about.html')
