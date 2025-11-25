from django.db import models

# Create your models here.
class Produce(models.Model):  #name of the table
    name = models.CharField(max_length=200)  #string
    price = models.IntegerField()  #numbers
