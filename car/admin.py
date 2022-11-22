from django.contrib import admin

from car.models import Car, Dealer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title',)



@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'car_display', 'contact', 'worker_hours')
    filter_horizontal = ('car',)

