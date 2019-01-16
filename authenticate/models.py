from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    collarNumber = models.CharField(max_length=50)
