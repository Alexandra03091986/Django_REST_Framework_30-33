from rest_framework.serializers import ModelSerializer

from users.models import Payments


class PaymentsSerializer(ModelSerializer):
    """Сериализатор для модели Платежи."""

    class Meta:
        """Метаданные сериализатора платежи."""
        model = Payments
        fields = "__all__"
