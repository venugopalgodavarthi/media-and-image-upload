from django.db import models

# Create your models here.
class imgupld(models.Model):
    img=models.ImageField(upload_to="%y/%m/%d")
    def __str__(self):
        return img.name