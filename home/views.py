from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "samar"
    }
    return render(request,'index.html',context)

def home(request):
    # return HttpResponse('this is home page')
    return render(request,'home.html')

def about(request):
    # return HttpResponse('this is about page')
    return render(request,'about.html')

def services(request):
    # return HttpResponse('this is service page')
    return render(request,'services.html')

def contact(request):
    # return HttpResponse('this is contact page')
    return render(request,'contact.html')

