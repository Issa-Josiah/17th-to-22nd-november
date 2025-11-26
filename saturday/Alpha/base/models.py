from django.db import models

# Create your models here.
class Base(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name