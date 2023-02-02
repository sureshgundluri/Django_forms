from django.shortcuts import render
from app.forms import *

def django_form(request):
    formobject=Studentform()
    d={'forms':formobject}
    if request.method=='POST':
        FD=Studentform(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            e=FD.cleaned_data['email']
            add=FD.cleaned_data['address']
            g=FD.cleaned_data['gender']
            c=FD.cleaned_data['courses']
            d1={'name':n,'age':a,'email':e,'address':add,'gender':g,'courses':c}
            return render(request,'data_form.html',d1)
        
    return render(request,'django_form.html',d)
