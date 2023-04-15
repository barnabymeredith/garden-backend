from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    name = models.CharField(max_length=600, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )

class Marker(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=120, null=True)
    top = models.FloatField(null=False)
    left = models.FloatField(null=False)
    picture = models.ForeignKey(
        Picture,
        on_delete=models.CASCADE,
        default=None
    )
    