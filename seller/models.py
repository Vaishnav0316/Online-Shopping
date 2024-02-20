from django.db import models
from Site_admin.models import *
from buyer.models import *
class seller_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DOB=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    PhoneNumber=models.CharField(max_length=20)
    File=models.FileField()
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Status=models.CharField(max_length=20,default="Pending")
class product_tb(models.Model):
    Name=models.CharField(max_length=20)
    File=models.FileField()
    Price=models.IntegerField()
    Stock=models.IntegerField()
    Details=models.CharField(max_length=20)
    Categoryid=models.ForeignKey('Site_admin.category_tb',on_delete=models.CASCADE)
    Sellerid=models.ForeignKey(seller_tb,on_delete=models.CASCADE)
class Tracking_tb(models.Model):
    Orderid=models.ForeignKey('buyer.order_tb',on_delete=models.CASCADE)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Details=models.CharField(max_length=20)


