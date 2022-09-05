from django.db import models

# Create your models here.
class Project(models.Model):
    ptitle=models.CharField(max_length=200)
    pdesc=models.TextField()
    ppic=models.CharField(max_length=120)
    giturl=models.CharField(max_length=500)