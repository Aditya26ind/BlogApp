from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import customcreationform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request,'index.html')
def signuppage(request):
    if request.method=="POST":
        form=customcreationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' request submitted successfully.')
            return render(request, 'signup.html', {'form':form})
    else:
        form=customcreationform()
    context={'form':form}
    return render(request,'signup.html',context)
def loginuser(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user) 
            return redirect('/news')
    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return redirect('/login')
def changePassword(request):
    if request.method=="POST":
        u = User.objects.filter(username=request.POST['username'])
        print(request.POST['username'])
        new=request.POST["new_password"]
        print(new)
        u.set_password(new)
        u.save()
    return render(request,'chngepass.html')