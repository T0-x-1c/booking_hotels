from django import forms
from hotel_system.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'date_start',
            'date_end',
            'phone',
            'persons'
        ]