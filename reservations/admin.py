from django.contrib import admin
from .models import Computer, FoodItem, Order, FoodCategory


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # Показываем изображение в списке
    fields = ('name', 'price', 'image', 'category')  # Разрешаем загрузку изображения

admin.site.register(Computer)
admin.site.register(FoodCategory)  # Добавлено
admin.site.register(FoodItem, FoodItemAdmin)  # Добавляем кастомный админ
admin.site.register(Order)
FoodCategory.objects.create(name='Кофе')
FoodCategory.objects.create(name='Десерт')