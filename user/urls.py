from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("index.html",views.index,name="home"),
    path("login.html",views.login,name="login"),
    path("feedback.html",views.feedback,name="feedback"),
    path("destinations.html",views.destinations,name="destinations"),
    path("paymentgateway.html",views.paymentgateway,name="paymentgateway"),
    path("paymentconfirmation.html",views.paymentcofirmation,name="paymentcofirmation"),
    path("admin",views.admin,name="admin")

]