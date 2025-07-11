from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TypeRoom(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
    
class Room(models.Model):
    number = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    place = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='rooms_image')
    type_room = models.ForeignKey(TypeRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f'room_number: {self.number}, price: {self.price}, place: {self.place}'
    
    class Meta:
        ordering = ['price']
        verbose_name = ['Кімната']
        verbose_name_plural = ['Кімнати']

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    date_creation= models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    persons = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"data start: {self.date_start}/ data end: {self.date_end}/ data creation: {self.date_creation}"

    class Meta:
        ordering = ['date_creation','date_start','date_end']
        verbose_name = "Reservation"  
        verbose_name_plural = "Reservations"

class Comment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Коментар від {self.user.username} до кімнати {self.room.number}'

    class Meta:
        ordering = ['-created_at']
