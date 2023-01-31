from django.db import models

# Create your models here.
class Homepost(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()