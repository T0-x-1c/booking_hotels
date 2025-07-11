from django.shortcuts import render, get_object_or_404, redirect
from hotel_system.forms import BookingForm, CommentForm
from hotel_system.models import Room, Booking, Comment

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = BookingForm()
    comment_form = CommentForm()
    comments = room.comments.all()

    if request.method == "POST":
        if 'reserve' in request.POST:
            form = BookingForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.room = room
                reservation.user = request.user
                reservation.save()
                return redirect('booking-room', room_id=room.id)

        elif 'comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.room = room
                comment.user = request.user
                comment.save()
                return redirect('booking-room', room_id=room.id)

    context = {
        'room': room,
        'form': form,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'booking.html', context)
