from django.shortcuts import render
import re
from django.http import HttpResponse


def home(request):
    
   
    return render(request, "Skstore/home.html")
