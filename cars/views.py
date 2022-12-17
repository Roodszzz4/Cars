
from django.shortcuts import render
from .models import Car, Dealer


def all_cars(request):
    cars = Car.objects.all()

    return render(request, 'base.html', {'cars': cars})



