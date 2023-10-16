from django.shortcuts import render
import re
from django.http import HttpResponse
from Skstore.models import Brand
from Skstore.models import Item

def home(request):
    
    brand = Brand.objects.all()
   
    return render(request, "Skstore/index.html", {'brand': brand})

def product(request, id):

    item = Item.objects.get(id=id)
    return render(request, "Skstore/product.html", {'item' : item})

def showcase(request):
    
    item = Item.objects.all()
    return render(request, "Skstore/showcase.html",
                  {'item': item})
