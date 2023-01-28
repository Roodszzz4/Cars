from django.shortcuts import render, get_object_or_404
from .models import Car, Dealer


def all_cars(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,

    }

    return render(request, 'all_cars.html', context=context)


def car_list(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    if search:
        context = {
            'cars': cars.filter(brand__istartswith=search)
        }
    else:
        context = {
            'cars': cars
        }
    return render(request, 'all_cars.html', context=context)


def one_car(request, pk):
    cars = get_object_or_404(Car, pk=pk)
    context = {
        "cars": cars
    }
    return render(request, 'one_car.html', context=context)