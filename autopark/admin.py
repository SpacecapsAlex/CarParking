from django.contrib import admin
from .models import Car, CarType, CarBrand

# Register your models here.

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarBrand)
