from django.db import models

class foods(models.Model):

    name = models.CharField(max_length=100,default='blank')
    price = models.IntegerField(default=0)
    description = models.TextField(default='blank')
    image = models.ImageField(upload_to='pics',default='blank',null=True)
    
    

class userinfo(models.Model):
    name = models.CharField(max_length=30,default='blank')
    email = models.EmailField(blank=True)
    number = models.IntegerField(default=0)
    password = models.IntegerField(default='')
    address = models.TextField(default='')
    pin = models.IntegerField(null=True)

class ownerinfo(models.Model):
    name= models.CharField(max_length=30,default='blank')
    password = models.IntegerField(default='')