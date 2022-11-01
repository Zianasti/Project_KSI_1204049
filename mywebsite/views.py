from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About")

def articles(request,year) :
    year=year
    str=year
    return HttpResponse(year)