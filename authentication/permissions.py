from rest_framework import permissions

class PublicUserPermission(permissions.BasePermission):
    message = 'Only user public permission...'

    def has_permission(self, request, view):
        if request.user.has_perm('authentication.user_public'):
            return True