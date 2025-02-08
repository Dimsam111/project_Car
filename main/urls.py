from django.urls import path

from .views import get_main_page, car_detail, car_add

urlpatterns = [
    path('',get_main_page, name='main'),
    path('car_detail/<int:id>',car_detail, name='car_detail'),
    path('car_add/', car_add, name='car_add'),
]
