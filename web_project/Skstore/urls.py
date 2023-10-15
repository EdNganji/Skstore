from django.urls import path
from Skstore import views

urlpatterns = [
    path('',views.home, name='home'),
    
]