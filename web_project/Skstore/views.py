from django.shortcuts import render
import re
from django.http import HttpResponse


def home(request):
    
   
    return render(request, "Skstore/index.html")

def product(request):

    return render(request, "Skstore/product.html")
