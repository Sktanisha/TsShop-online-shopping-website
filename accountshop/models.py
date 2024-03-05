from django.db import models

# Create your models here.

class items(models.Model):
    name_item = models.CharField(max_length = 30)
    price = models.FloatField()
    availability = models.CharField()
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    