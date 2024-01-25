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
            CarType(name='SUV'),
            CarType(name='Crossover'),
            CarType(name='Coupe'),
            CarType(name='Convertible'),
            CarType(name='Pickup'),
            CarType(name='Wagon'),
            CarType(name='Van'),
            CarType(name='Limousine'),
            CarType(name='Roadster'),
            CarType(name='MPV'),
        ]

        car_brands = [
            CarBrand(name='Audi'),
            CarBrand(name='BMW'),
            CarBrand(name='Chevrolet'),
            CarBrand(name='Citroen'),
            CarBrand(name='Dacia'),
            CarBrand(name='Fiat'),
            CarBrand(name='Ford'),
            CarBrand(name='Honda'),
            CarBrand(name='Hyundai'),
            CarBrand(name='Kia'),
            CarBrand(name='Lada'),
            CarBrand(name='Lexus'),
            CarBrand(name='Mazda'),
            CarBrand(name='Mercedes-Benz'),
            CarBrand(name='Mitsubishi'),
            CarBrand(name='Nissan'),
            CarBrand(name='Opel'),
            CarBrand(name='Peugeot'),
            CarBrand(name='Renault'),
            CarBrand(name='Seat'),
            CarBrand(name='Skoda'),
            CarBrand(name='Suzuki'),
            CarBrand(name='Toyota'),
            CarBrand(name='Volkswagen'),
            CarBrand(name='Volvo'),
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
            ParkingSlot(number=5),
            ParkingSlot(number=6),
            ParkingSlot(number=7),
            ParkingSlot(number=8),
            ParkingSlot(number=9),
            ParkingSlot(number=10),
        ]

        park_slots_2 = [
            ParkingSlot(number=1),
            ParkingSlot(number=2),
            ParkingSlot(number=3),
            ParkingSlot(number=4),
            ParkingSlot(number=5),
            ParkingSlot(number=6),
            ParkingSlot(number=7),
            ParkingSlot(number=8),
            ParkingSlot(number=9),
            ParkingSlot(number=10),
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
