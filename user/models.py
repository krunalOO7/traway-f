from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    
    location = models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Trip(models.Model):
    name=models.CharField(max_length=50)
    trip_image= models.ImageField(upload_to='trip_image/',null=True,blank=True)
    trip_image1= models.ImageField(upload_to='trip_image/',null=True,blank=True)
    trip_image2= models.ImageField(upload_to='trip_image/',null=True,blank=True)
    days = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=600)
    COUNTRY = (
        ("India","India"),
        ("UAE","UAE"),
        ("Bhutan","Bhutan"),
        ("Thailand","Thailand"),
        ("Nepal","Nepal"),
    )
    country = models.CharField(max_length=50,null=True,choices=COUNTRY)
    create_date= models.DateField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Trip',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
