from django.db import models
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Модель компьютера для бронирования
class Computer(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)  # Название категории (например, Кофе, Десерт, Еда)
    description = models.TextField(blank=True, null=True)  # Описание категории

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='items')  # Связь с категорией

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food_item.name}"


class OrderHistoryView(TemplateView):
    template_name = 'reservations/order_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)  # Предполагается, что у вас есть модель Order
        return context
