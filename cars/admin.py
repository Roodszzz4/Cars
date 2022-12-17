from django.contrib import admin
from .models import Car, Dealer


class CarInLine(admin.TabularInline):
    model = Car.dealer.through


class DealerInLine(admin.TabularInline):
    model = Car.dealer.through


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'dealer_display', ]
    filter_horizontal = ['dealer', ]
    inlines = [DealerInLine, ]


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'contact', 'worker_hours', ]
    inlines = [CarInLine, ]
