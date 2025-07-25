from django import forms
from hotel_system.models import Booking
from .models import Comment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'date_start',
            'date_end',
            'phone',
            'persons'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ваш коментар...'}),
        }

