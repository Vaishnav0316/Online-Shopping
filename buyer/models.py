from django.db import models
from seller.models import *
from Site_admin.models import *
class buyer_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DOB=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    PhoneNumber=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class cart_tb(models.Model):
    Productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    Buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Total=models.IntegerField()
class order_tb(models.Model):
    customer_name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Phonenumber=models.CharField(max_length=20)
    Buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    GrandTotal=models.IntegerField()
    OrderDate=models.CharField(max_length=20)
    OrderTime=models.CharField(max_length=20)
    Status=models.CharField(max_length=20,default="Pending")
class orderitems_tb(models.Model):
    Orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)
    Productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    Buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Total=models.IntegerField()
class pay_tb(models.Model):
    Name=models.CharField(max_length=20)
    CardNumber=models.CharField(max_length=20)
    CVV=models.CharField(max_length=20)
    Exp_Date=models.CharField(max_length=20)
    Buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    Orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)


    
