from django.urls import path, include
from . import views

urlpatterns = [
    path('inititialize/', views.initialize, name='initialize'),
    path('get-cars/', views.get_cars, name='get-cars'),
]
