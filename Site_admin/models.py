from django.db import models
class admin_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class category_tb(models.Model):
    Category_Name=models.CharField(max_length=20)