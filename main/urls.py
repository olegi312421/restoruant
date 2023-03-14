from django.urls import path, include
from .views import update_reservation, main, list_reservations


app_name = 'main'

urlpatterns = [
    path('', main),
    path('manager/update_reserve/<int:pk>', update_reservation, name='update_reservation'),
    path('manager/reserve_list/', list_reservations, name='list_reservation'),
]