from django.db import models


class Brand(models.Model):
    
    name = models.CharField(max_length=100)
    id = models.PositiveSmallIntegerField(default=0, primary_key=True)
    image = models.ImageField(upload_to='Skstore/files/images')
    mailFournisseur = models.EmailField()
    Num = models.CharField(max_length=10)
    

class Item(models.Model):
    
    name = models.CharField(max_length=100)
    id = models.PositiveSmallIntegerField(default=0, primary_key=True)
    image = models.ImageField(upload_to='Skstore/files/images')
    price = models.DecimalField(max_digits=5, decimal_places = 2, default=0)
    Brand = models.ForeignKey(Brand, null=False, on_delete=models.CASCADE)
    