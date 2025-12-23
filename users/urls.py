from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet

app_name = UsersConfig.name
# Создание роутера
router = DefaultRouter()
# Регистрация ViewSet
router.register(r"payments", PaymentViewSet)

urlpatterns = [
    path("", include(router.urls))
]
