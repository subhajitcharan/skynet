from django.db import models

class foods(models.Model):
    name = models.CharField(max_length=100,default='blank')
    price = models.IntegerField(default=0)
    description = models.TextField(default='blank')
    image = models.ImageField(upload_to='pics',default='blank',null=True)
    
class extrauserinfo(models.Model):
    name= models.CharField(max_length=100,default='blank')
    number= models.CharField(max_length=10,null=True)
    address= models.TextField(default='blank')
    pin= models.CharField(max_length=6,null=True)
    email= models.EmailField(null=True)

class orderinfo(models.Model):
    username=models.CharField(max_length=100,default='blank')
    address=models.TextField(max_length=500,default='blank')
    order=models.TextField(max_length=1000,default='blank')


