from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentViewSet(ModelViewSet):
    """ViewSet для платежей с фильтрацией:
    1. Сортировка по дате оплаты (ordering)
    2. Фильтрация по курсу или уроку
    3. Фильтрация по способу оплаты"""
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['course_paid', 'lesson_paid', 'method_payment']
    ordering_fields = ['date_payment']
    # Сортировка по умолчанию (новые первыми)
    ordering = ['-date_payment']
