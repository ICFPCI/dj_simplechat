from rest_framework import permissions

class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_staff:
            return True
        else:
            return view.action in ['create', 'retrieve', 'update']   
        
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        
        if request.user != obj:
            return False
        
        return True