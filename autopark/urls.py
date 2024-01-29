from django.urls import path, include
from . import views

urlpatterns = [
    path('inititialize/', views.initialize, name='initialize'),
    path('get-cars/', views.get_cars, name='get-cars'),
    path('get-car-by-id/<int:car_id>/', views.get_car_by_id, name='get-car-by-id'),
]
