from rest_framework.permissions import BasePermission, IsAuthenticated



class IsManager(BasePermission):
    """
    Allows access only to managers.
    """

    def has_permission(self, request, view):
        return bool(request.user.groups.filter(name='Manager').exist())

class IsCustomer(BasePermission):
    """
    Allows access only to customers.
    Users not assigned to a group will be considered customers.
    """

    def has_permission(self, request, view):
        if (not request.user.groups.filter(name='Manager').exist()) and (not request.user.groups.filter(name='Delivery_crew').exist()):
            if request.user.is_authenticated:
                return True
            
        return False
    
class IsDeliveryCrew(BasePermission):
    """
    Allows access only to delivery crew.
    """

    def has_permission(self, request, view):
        return bool(request.user.groups.filter(name='Delivery_crew').exist())

class IsCustomerOrDeliveryCrew(BasePermission):
    """
    Allows access only to customers or delivery crew.
    """

    def has_permission(self, request, view):
        return IsCustomer or IsDeliveryCrew
    
