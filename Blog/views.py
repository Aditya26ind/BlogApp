from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import blogmodels
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login')
def blog(request):
    userdata=request.user
    if request.method=="POST":
        blogs=request.POST['blogwritten']
        titles=request.POST['title']
        dts=blogmodels.objects.create(user_id=userdata.id,textblog=blogs,title=titles)
        dts.save()
    data=blogmodels.objects.filter(user_id=userdata.id)
    return render(request,'blog.html',{'data':data})
@login_required(login_url='/login')
def blogdelete(request,pk):
    userdata=request.user
    if request.method=="POST":
        blogmodels.objects.filter(user_id=userdata.id).filter(id=pk).delete()
        return redirect('/blog')

