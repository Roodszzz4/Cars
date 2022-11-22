from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Dealer(models.Model):
    title = models.CharField(max_length=55)
    address = models.CharField(max_length=255)
    contact = models.IntegerField(blank=True, null=True)
    worker_hours = models.TextField(default="", blank=True )
    car = models.ManyToManyField(Car, blank=True)

    def car_display(self):
        return ', '.join([car.title for car in self.car.all()])

    car_display.short_description = 'Cars'


