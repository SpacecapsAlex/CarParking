from django.http import HttpResponse
from django.shortcuts import render
from .models import CarType, CarBrand, Car, ParkingSlot, Parking

# Create your views here.


def initialize(request):
    try:
        car_types = [
            CarType(name='Sedan'),
            CarType(name='Hatchback'),
            CarType(name='Minivan'),
        ]

        car_brands = [
            CarBrand(name='Audi'),
            CarBrand(name='BMW'),
            CarBrand(name='Chevrolet'),
        ]

        parks = [
            Parking(name='Parking 1', address='Address 1', phone_number='Phone 1', price=1.0),
            Parking(name='Parking 2', address='Address 2', phone_number='Phone 2', price=2.0),
        ]

        park_slots_1 = [
            ParkingSlot(number=1),
            ParkingSlot(number=2),
            ParkingSlot(number=3),
            ParkingSlot(number=4),
        ]

        park_slots_2 = [
            ParkingSlot(number=1),
            ParkingSlot(number=2),
            ParkingSlot(number=3),
            ParkingSlot(number=4),
        ]

        for car_type in car_types:
            car_type.save()

        for car_brand in car_brands:
            car_brand.save()

        for i in range(1, 11):
            car = Car(car_number=f'AA{i}AA{i}', car_type=car_types[0], car_brand=car_brands[0], is_electric=False, year=2000)
            car.save()

        for park in parks:
            park.save()

        for slot in park_slots_1:
            slot.save()
            slot.parking = parks[0]
            slot.save()

        for slot in park_slots_2:
            slot.save()
            slot.parking = parks[1]
            slot.save()

        return HttpResponse('Success')

    except:
        return HttpResponse('Error')


def get_cars(request):
    cars = Car.objects.all()
    return render(request, 'autopark/cars.html', {'cars': cars})


def get_car_by_id(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'autopark/get_car_by_id.html', {'car': car})
