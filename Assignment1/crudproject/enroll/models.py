from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    city= models.CharField(max_length=60)
    pincode= models.CharField(max_length=60)
    password= models.CharField(max_length=50)
