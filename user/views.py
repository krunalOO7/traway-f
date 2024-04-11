from django.shortcuts import render

def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def destinations(request):
    return render(request,"destinations.html")

def feedback(request):
    return render(request,"feedback.html")

def paymentgateway(request):
    return render(request,"paymentgateway.html")

def paymentcofirmation(request):
    return render(request,"paymentconfirmation.html")

def admin(request):
    return render(request,"admin.html")





# Create your views here.
