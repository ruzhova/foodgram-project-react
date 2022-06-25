from rest_framework import permissions


class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if (request.method in ['PUT', 'PATCH', 'DELETE'] and
           not request.user.is_anonymous):
            return (
                request.user == obj.author
                or request.user.is_staff
                or request.user.is_superuser
            )
        return request.method in permissions.SAFE_METHODS
