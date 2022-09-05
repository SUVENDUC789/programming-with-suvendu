from statistics import mode
from django.db import models

# Create your models here.
# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    message=models.TextField()
    date=models.DateField()

    