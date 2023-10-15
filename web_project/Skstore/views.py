from django.shortcuts import render
import re
from django.http import HttpResponse
from Skstore.models import Brand

def home(request):
    
    brand = Brand.objects.all()
   
    return render(request, "Skstore/index.html", {'brand': brand})

def product(request):

    return render(request, "Skstore/product.html")
