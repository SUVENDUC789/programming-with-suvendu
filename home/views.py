from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
p = {
    'programmer': "Suvendu Chowdhury",
    'use': "Django"
}


def index(request):
    return render(request, 'index.html', p)


def about(request):
    return render(request, 'about.html', p)


def contact(request):
    return render(request, 'contact.html', p)
