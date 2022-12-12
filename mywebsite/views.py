from django.http import HttpResponse
from django.shortcuts import render

from . import forms

def index(request):
    return render(request, 'index.html')

def form(request):
    classform = forms.classform()
    context = {'heading' : 'FORM',
    'classform' : classform
    }
    if request.method == 'POST':
        print("Ini adalah method post")
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
        context['namac'] = request.POST['namac']
        context['alamatc'] = request.POST['alamatc']
    else:
        print("Ini adalah method get")

    return render(request, 'form.html', context)

def about(request):
    return HttpResponse("About")

def articles(request,year) :
    year=year
    str=year
    return HttpResponse(year)