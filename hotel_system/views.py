from django.shortcuts import render
from hotel_system.models import Room, TypeRoom, Booking

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    context = {
        'message': 'password:123',
        'rooms' : rooms,
    }
    return render(request, template_name='room_list.html', context=context)

