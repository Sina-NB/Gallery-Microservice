from django.db import models

# Create your models here.
class Photo(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)