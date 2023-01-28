from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_cars),
    path('car_search/', views.car_list, name='car_list'),
    path('<int:pk>/', views.one_car, name='one_car'),

]
