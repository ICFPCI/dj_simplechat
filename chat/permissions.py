from rest_framework.permissions import BasePermission

class ConversationPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False
    
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        
        if not request.user in obj.users.all():
            return False
        return True