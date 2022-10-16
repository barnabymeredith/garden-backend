from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=3
    )

class Marker(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=120, null=True)
    top = models.FloatField(null=False)
    left = models.FloatField(null=False)
    #picture = models.ForeignKey(
    #    Picture,
    #    on_delete=models.CASCADE,
    #    default=3
    #)
    