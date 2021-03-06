from django.db import models

# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    img= models.ImageField(upload_to='pics')
    prize= models.IntegerField()
    offer= models.BooleanField(default=False)
