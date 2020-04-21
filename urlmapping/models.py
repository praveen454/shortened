from django.db import models

# Create your models here.
class ShortendUrl(models.Model):
    longurl = models.CharField(max_length=500)
    shorturl = models.CharField(max_length=50)
