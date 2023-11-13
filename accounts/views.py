from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from  .forms import user_r_f,user_l_f
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

def user_r (request) :
    if request.method == 'POST':        
        form=user_r_f(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            
            user.save()
            login(request,user)
            messages.success(request,'register successfully','success')
            return redirect('hello')
    else:
        form=user_r_f()
        return render(request,'register.html',{'form':form})


def user_l (request) :
    if request.method == 'POST':        
        form=user_l_f(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'logged in successfully','success')
                return redirect('hello')
            else:
               messages.error(request,'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.','danger')
    else:
        form=user_l_f()
    return render(request,'login.html',{'form':form})

def user_out(request):
    logout(request)
    messages.success(request,'logout successfully','success')
    return redirect('hello')


