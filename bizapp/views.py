from django.shortcuts import render


def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"home-2.html")


def contact(request):
    return render(request,"contact.html")


def about(request):
    
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")