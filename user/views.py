from django.shortcuts import render
from django.conf import settings

def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def destinations(request):
    return render(request,"destinations.html")

def checkout(request):
    return render(request,"checkout.html")

def feedback(request):
    return render(request,"feedback.html")

def paymentgateway(request):
    return render(request,"paymentgateway.html")

def paymentcofirmation(request):
    return render(request,"paymentconfirmation.html")

def admin(request):
    return render(request,"admin.html")

def error_404_view(request, exception):
    return render(request, '404.html')







# Create your views here.
