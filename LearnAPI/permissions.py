from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Returns a boolean indicating whether the user has read access by default.
    If not it checks if the user is the owner of the object
    """


def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
        return True
    return obj.owner == request.user
