from django.db import models



# Create your models here.
class Brand(models.Model):
    
    name = models.CharField(max_length=100)
    id = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='files/images')
    