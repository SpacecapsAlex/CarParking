from django.db.models import Q
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from .models import CarType, CarBrand, Car, ParkingSlot, Parking
from django.contrib.auth.decorators import login_required, permission_required


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
    brand_list = CarBrand.objects.all()
    type_list = CarType.objects.all()

    data = {
        'car': car,
        'brands': brand_list,
        'types': type_list
    }

    return render(request, 'autopark/get_car_by_id.html', data)


"""
Обновляет объект автомобиля с предоставленной информацией из HttpRequest.

Параметры:
    request (HttpRequest): Объект HTTP-запроса.
    car_id (int): Идентификатор обновляемого автомобиля.

Возвращает:
    HttpResponseRedirect: Перенаправляет на URL 'get-cars' после обновления автомобиля.
"""
def update_car(request: HttpRequest, car_id: int):
    if request.method != 'POST':
        return HttpResponse('Invalid request method')

    car = Car.objects.get(id=car_id)

    car_year = request.POST.get('year')
    car_is_electric = request.POST.get('is_electric')
    car_type_id = request.POST.get('car_type_id')
    car_brand_id = request.POST.get('car_brand_id')

    car_type = CarType.objects.get(id=car_type_id)
    car_brand = CarBrand.objects.get(id=car_brand_id)

    car.car_type = car_type
    car.car_brand = car_brand
    car.year = car_year
    car.is_electric = car_is_electric == 'on'

    car.save()

    return HttpResponseRedirect(reverse('get-cars'))


"""
Удаляет автомобиль с заданным car_id из базы данных.

Параметры:
- request: объект HttpRequest
- car_id: int, ID удаляемого автомобиля

Возвращает:
- объект HttpResponseRedirect, перенаправляющий на URL 'get-cars'
"""
def delete_car(request: HttpRequest, car_id: int):
    car = Car.objects.get(id=car_id)
    car.delete()
    return HttpResponseRedirect(reverse('get-cars'))  # reverse - возвращает URL по имени представления


#@login_required  # декоратор, требующий аутентификации пользователя
@permission_required('car.p1')  # декоратор, требующий наличия определенных разрешений
def add_car(request):
    """
    Представление для добавления нового автомобиля в автопарк.
    Обрабатывает как GET, так и POST запросы.
    Для GET запросов извлекает список марок и типов автомобилей и рендерит шаблон 'add_car.html' с данными.
    Для POST запросов извлекает детали автомобиля из запроса и сохраняет новый автомобиль в базу данных, затем перенаправляется на URL 'get-cars'.
    """
    if request.method == 'GET':
        brand_list = CarBrand.objects.all()
        type_list = CarType.objects.all()

        data = {
            'brands': brand_list,
            'types': type_list
        }

        return render(request, 'autopark/add_car.html', data)

    if request.method == 'POST':
        car_number = request.POST.get('car_number')
        car_type_id = request.POST.get('car_type_id')
        car_brand_id = request.POST.get('car_brand_id')
        is_electric = request.POST.get('is_electric')
        year = request.POST.get('year')

        car_type = CarType.objects.get(id=car_type_id)
        car_brand = CarBrand.objects.get(id=car_brand_id)

        car = Car(
            car_number=car_number,
            car_type=car_type,
            car_brand=car_brand,
            is_electric=is_electric == 'on',
            year=year
        )
        car.save()

        return HttpResponseRedirect(reverse('get-cars'))


"""
Функция для поиска автомобилей по номеру, типу и бренду.

Параметры:
- request: объект HTTP-запроса

Возвращает:
- Если метод запроса 'GET', отображает шаблон 'autopark/cars.html'.
- Если метод запроса не 'GET', фильтрует объекты Car на основе строки поиска и отображает шаблон 'autopark/cars.html' с отфильтрованным списком автомобилей.
"""
def search_car(request):
    if request.method == 'GET':
        return render(request, 'autopark/cars.html')
    else:
        search_string = request.POST.get('search_string')
        car_list = Car.objects.filter(
            Q(car_brand__name__icontains=search_string)
            | Q(car_type__name__icontains=search_string)
            | Q(car_number__icontains=search_string)
        )

        return render(request, 'autopark/cars.html', {'cars': car_list})
