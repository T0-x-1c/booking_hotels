# urls.py
from django.urls import path
from .views import room_list, booking

urlpatterns = [
    path('', room_list, name='room-list'),
    path('booking/<int:room_id>', booking, name='booking-room'),

]