from django.db import models

# Create your models here.

class items(models.Model):
    name_item = models.CharField(max_length = 30)
    price = models.FloatField()
    availability = models.CharField(max_length = 20)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

class profile(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    confpassword = models.CharField(max_length = 20)
    email=models.EmailField(max_length=30)
    contact = models.IntegerField(max_length=11)

class item_test(models.Model):
    tname_item = models.CharField(max_length = 30)
    tprice = models.FloatField()
    tavailability = models.BooleanField()
    tpicture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)