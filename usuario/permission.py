from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method == 'POST' or request.user.is_authenticated)
