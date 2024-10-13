from django.urls import path
from .views import HomeView, duty_page, CustomLogoutView, order_history, get_started, signup, login_view, order_food, food_category
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reservations'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Выход
    path('duty/', duty_page, name='duty-page'),  # Страница обязанностей
    path('get-started/', get_started, name='get-started'),  # Начать работу
    path('signup/', signup, name='signup'),  # Регистрация
    path('login/', login_view, name='login'),  # Вход
    path('order-food/', order_food, name='order_food'),  # Заказ еды
    path('order-history/', order_history, name='order_history'),  # История заказов
    path('food/<str:category_name>/', food_category, name='food_category'),  # Изменено на category_name
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
