from django.db import models 

class Widgets(models.Model):
    description = models.CharField(max_length=50) 
    quantity = models.IntegerField()


# Create your models here.
