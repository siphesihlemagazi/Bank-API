from rest_framework.permissions import BasePermission

from api.models import Account


class IsAccountOwner(BasePermission):
    """
    Allows access only to admin and account owner.
    """

    def has_permission(self, request, view):
        access = False
        if request.user.is_staff or request.user == Account.holder:
            access = True
        return access
