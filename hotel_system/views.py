from django.shortcuts import render, get_object_or_404
from hotel_system.forms import BookingForm
from hotel_system.models import Room, TypeRoom, Booking

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms' : rooms,
    }
    return render(request, template_name='room_list.html', context=context)

def booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.user = request.user
            reservation.save()
    context = {
        'room': room,
        'form': form
    }
    return render(request, template_name='booking.html', context=context)

