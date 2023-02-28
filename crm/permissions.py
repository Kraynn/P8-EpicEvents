from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import User


class ClientPermission(BasePermission):

    def has_permission(self, request, view):
        view_action = ['list', 'retrieve']
        action = ['create', 'update', 'destroy']
        sales_group = User.objects.get(username=request.user).groups.filter(name='sales').exists()
        support_group = User.objects.get(username=request.user).groups.filter(name='support').exists()

        if view.action in view_action:
            if sales_group is True:
                return True
            elif support_group is True:
                return True

        elif view.action in action:
            if sales_group is True:
                return True
            else:
                raise PermissionDenied(detail='User has to be sales')
            

class ContractPermission(BasePermission):

    def has_permission(self, request, view):
        action = ['list', 'retrieve', 'create', 'update']
        sales_group = User.objects.get(username=request.user).groups.filter(name='sales').exists()

        if view.action in action:
            if sales_group is True:
                return True
            else:
                raise PermissionDenied(detail='User has to be sales')

        elif view.action == 'destroy':
            return False
        

class EventPermission(BasePermission):

    def has_permission(self, request, view):
        support_team_action = ['list', 'retrieve', 'update']
        sales_team_action = ['create']
        sales_group = User.objects.get(username=request.user).groups.filter(name='sales').exists()
        support_group = User.objects.get(username=request.user).groups.filter(name='support').exists()

        if view.action in support_team_action:
            if support_group is True:
                return True
            else:
                raise PermissionDenied(detail='User has to be support')

        elif view.action in sales_team_action:
            if sales_group is True:
                return True
            else:
                raise PermissionDenied(detail='Sales has to be support')

        elif view.action == 'destroy':
            return False