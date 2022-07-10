from django.shortcuts import redirect, render
import requests
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url='/login')
# def homeview(request):
#     if request.method=="POST":
#         searched=request.POST['search']
#         data=requests.get(f"https://newsapi.org/v2/everything?q={searched}&from=2021-08-30&sortBy=publishedAt&apiKey=680e06c9e1be4252acdb6b31b289a09a").json()
#         return render(request,'home.html',{'data':data})
#     else:
#         data=requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-08-30&sortBy=publishedAt&apiKey=680e06c9e1be4252acdb6b31b289a09a").json()
#         return render(request,'home.html',{'data':data})


@login_required(login_url='/login')
def homeview(request):
    if request.method=="POST":
        url = "https://api.newscatcherapi.com/v2/search"
        searched=request.POST['search']
        querystring = {"q":f"{searched}","lang":"en","sort_by":"relevancy","page":"1"}

        headers = {
            "x-api-key": "tCyIhc_7L7Gf28ocJh9UdVFQiS3zGEwct_S1_v8edn8"
            }

        response = requests.get(url, headers=headers, params=querystring)
        return render(request,'home.html',{'data':response})
    url = "https://api.newscatcherapi.com/v2/search"
    querystring = {"q":"Elon Musk","lang":"en","sort_by":"relevancy","page":"1"}

    headers = {
        "x-api-key": "tCyIhc_7L7Gf28ocJh9UdVFQiS3zGEwct_S1_v8edn8"
        }
    response = requests.get(url, headers=headers, params=querystring)
    return render(request,'home.html',{'data':response})
