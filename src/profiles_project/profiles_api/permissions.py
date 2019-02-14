from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS: #check if the request is in safe permission method (not delete, destroy)
            return True

        return obj.id == request.user.id #check if the user requesting a change is editing its profile
