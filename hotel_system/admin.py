from django.contrib import admin
from hotel_system.models import Room, Booking, TypeRoom

# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(TypeRoom)