from rest_framework import permissions

class IsModer(permissions.BasePermission):
    """Permission для проверки принадлежности пользователя к группе модераторов.

    Проверяет, состоит ли аутентифицированный пользователь в группе с названием
    "moderators". Если пользователь не аутентифицирован или не состоит в указанной
    группе, доступ запрещается."""
    def has_permission(self, request, view):
        """Проверяет право доступа пользователя к представлению."""
        return request.user.groups.filter(name="moderators").exists()
