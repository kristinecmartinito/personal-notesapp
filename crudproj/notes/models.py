from unicodedata import name
from django.db import models

# Create your models here.

class Notes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
