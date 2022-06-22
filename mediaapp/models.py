from django.db import models

class Imgmodel(models.Model):
    title=models.CharField(max_length=250)
    image_name=models.ImageField()
