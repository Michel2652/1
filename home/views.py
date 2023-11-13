from django.shortcuts import render,redirect
from .models import person
from django.contrib import messages
from .form import pf,npf

# Create your views here.

def h (request):
    p=person.objects.all()
    return render (request,'hello.html',{'p':p})

def g (request):
    return render (request,'goodby.html')

def x (request,x):
    g=person.objects.get(id=x)
    return render (request,'x.html',{'g':g})

def delete (request,id):
    person.objects.get(id=id).delete()
    messages.success(request,'delete successfully','success')
    return redirect ('hello')

def create (request) :
    if request.method == 'POST':        
        form=pf(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            person.objects.create(first_name=cd['f1'],last_name=cd['f2'])
            messages.success(request,'create successfully','success')
            return redirect('hello')
    else:
        form = pf()
    return render(request,'create.html',{'form':form})

def update (request,p_id) :
    p=person.objects.get(id=p_id)
    if request.method == 'POST':        
        form=npf(request.POST,instance=p)
        if form.is_valid():
            form.save()
            messages.success(request,'update successfully','success')
            return redirect('profile',p_id)
    else:
        form=npf(instance=p)
    return render(request,'update.html',{'form':form})

def welcom (request):
    return render (request,'welcom.html')
