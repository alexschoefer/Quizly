from rest_framework.permissions import BasePermission

class IsOwnerOfTheQuiz(BasePermission):
    """
    Custom permission to only allow owners of a quiz to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        """"
        Check if the user making the request is the owner of the quiz object.
        """
        return obj.owner == request.user
    
    def has_permission(self, request, view):
        """
        Check if the user is authenticated before allowing access to the view.
        """
        return request.user and request.user.is_authenticated