from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Для выполнения данного действия требуются права владельца объекта"

    def has_object_permission(self, request, view, obj):
        if request.user.role == obj.user:
            return True
        return False
