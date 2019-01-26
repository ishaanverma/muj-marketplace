from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # Custom User permission to allow owners of an object to edit it

    def has_object_permission(self, request, view, obj):
        # Read permission is allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission allowed only to creater of object
        return obj.user == request.user
