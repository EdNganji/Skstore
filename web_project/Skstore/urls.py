from django.urls import path
from Skstore import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product, name='product'),
    path('showcase/', views.showcase, name='showcase'),
    
]