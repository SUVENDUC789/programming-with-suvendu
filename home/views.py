from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from projectshandle.models import Project
from django.contrib import messages

p = {
    'programmer': "Suvendu Chowdhury",
    'use': "Django"
}


def index(request):
    return render(request, 'index.html', p)
    
def error_404(request,exception):
    return render(request, 'error.html', p)


def about(request):
    serviceData=Project.objects.all()
    pdata = {
        'programmer': 'Suvendu Chowdhury',
        'use': 'Django',
        'serviceData': serviceData,
    }
    return render(request, 'about.html', pdata)


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name','default')
        phone=request.POST.get('phone','default')
        email=request.POST.get('email','default')
        msg=request.POST.get('msg','default')
        en=Contact(name=name,phone=phone,email=email,message=msg,date=datetime.today())
        en.save()
        masspass=f'{name} message has been sent '
        messages.success(request, masspass)
    return render(request, 'contact.html', p)



