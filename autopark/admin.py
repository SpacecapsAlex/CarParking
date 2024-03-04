from django.contrib import admin
from .models import Car, CarType, CarBrand
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarBrand)
admin.site.register(Permission)
