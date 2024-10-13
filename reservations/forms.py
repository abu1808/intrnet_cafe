from django import forms
from .models import Order, Reservation

# Форма для создания заказа еды
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['food_item', 'quantity']

# Форма для бронирования компьютера
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['computer', 'date_reserved']
