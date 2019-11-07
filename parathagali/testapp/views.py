from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request,"testapp/home.html")
def f2(request):
    return render(request,"testapp/about.html")
def f3(request):
    return render(request,"testapp/learn.html")
def f4(request):
    return render(request,"testapp/location.html")
def f5(request):
    return render(request,"testapp/contact.html")
