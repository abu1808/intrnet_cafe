from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import FoodItem, Order, FoodCategory
from django.contrib.auth.decorators import login_required

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('reservations:home')  # Перенаправление на домашнюю страницу после выхода

class HomeView(TemplateView):
    template_name = 'reservations/home.html'  # Шаблон для главной страницы

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user  # Передача информации о пользователе в шаблон
        return context


@login_required
def food_category(request, category_name):
    categories = FoodCategory.objects.filter(name__iexact=category_name)

    if categories.exists():
        category = categories.first()  # Получаем первую категорию из результатов
        food_items = category.items.all()  # Получаем все продукты в данной категории
        return render(request, 'reservations/food_category.html', {'category': category, 'food_items': food_items})

    return render(request, 'reservations/404.html', status=404) 

@login_required
def order_food(request):
    food_items = FoodItem.objects.all()

    if request.method == "POST":
        food_item_id = request.POST.get("food_item")
        quantity = request.POST.get("quantity")
        food_item = get_object_or_404(FoodItem, id=food_item_id)

        # Сохраняем заказ в базу данных
        order = Order.objects.create(user=request.user, food_item=food_item, quantity=quantity)

        return render(request, 'reservations/order_confirmation.html', {
            'food_item': food_item,
            'quantity': quantity,
            'total_price': food_item.price * int(quantity),
        })

    return render(request, 'reservations/order_food.html', {
        'food_items': food_items,
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'reservations/order_history.html', {
        'orders': orders,
    })

def duty_page(request):
    return render(request, 'reservations/duty_page.html')  # Шаблон страницы обязанностей

def get_started(request):
    return render(request, 'reservations/getstarted.html')  # Шаблон страницы "Начать работу"

def signup(request):
    return render(request, 'reservations/signup.html')  # Шаблон страницы регистрации

def login_view(request):
    return render(request, 'reservations/login.html')  # Шаблон страницы входа
