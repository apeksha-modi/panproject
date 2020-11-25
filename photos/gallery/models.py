from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Image(models.Model):
    #name = models.TextField(max_length='100')
    path =models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
