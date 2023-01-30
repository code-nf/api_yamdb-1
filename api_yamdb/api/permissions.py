from rest_framework import permissions



class IsAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.user == request.user)



class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
         if request.method in permissions.SAFE_METHODS:
           return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
           return True
        return (request.user.is_moderator or request.user.is_staff)
       


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
           return True
        return bool(request.user.is_admin and request.user.is_staff)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
           return True
        return bool(request.user.is_admin and request.user.is_staff)



class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
         if request.method in permissions.SAFE_METHODS:
           return True

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_moderator
            or request.user.is_admin
            or obj.author == request.user
        )