from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' and request.user.is_authenticated:
            return True

        if request.method == 'POST' and request.user.is_authenticated is False:
            return True

        return False
