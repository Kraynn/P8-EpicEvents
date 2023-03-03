from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django.core.exceptions import ValidationError
from .serializers import Registerializer, ClientSerializer, ContractSerializer, EventSerializer
from .permissions import ClientPermission, ContractPermission, EventPermission
from .models import User, Client, Contract, Event


class RegisterViewset(ModelViewSet):
    serializer_class = Registerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    filter_backends = [SearchFilter]
    search_fields = ['last_name', 'email']

    def get_queryset(self):
        current_user = self.request.user
        if current_user.groups.filter(name='sales').exists() is True:
            return Client.objects.filter(sales_contact=current_user)
        elif current_user.groups.filter(name='support').exists() is True:
            events = Event.objects.filter(support_contact=current_user)
            clients_filter = events.values('client')
            return Client.objects.filter(id__in=clients_filter)

    def perform_create(self, serializer):
        current_user = self.request.user
        data = {'sales_contact': current_user}
        serializer.save(**data)

                
class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPermission]
    filter_backends = [SearchFilter]
    search_fields = ['client__last_name', 'client__email', 'date_created', 'amount']

    def get_queryset(self):
        return Contract.objects.filter(sales_contact=self.request.user)

    def perform_create(self, serializer):
        current_user = self.request.user
        data = {'sales_contact': current_user, 'status': True}
        serializer.save(**data)


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermission]
    filter_backends = [SearchFilter]
    search_fields = ['client__last_name', 'client__email', 'event_date']

    def get_queryset(self):
        return Event.objects.filter(support_contact=self.request.user)

    def perform_create(self, serializer):
        support = serializer.validated_data.get('support_contact')
        support_group = User.objects.get(username=support).groups.filter(name='support').exists()
        if support_group is True:
            client_id = serializer.validated_data['contract'].client
            data = {'client': client_id}
            serializer.save(**data)
        else:
            raise ValidationError('User is not support')

    def perform_update(self, serializer):
        support = serializer.validated_data.get('support_contact')
        support_group = User.objects.get(username=support).groups.filter(name='support').exists()
        if support_group is True:
            client_id = serializer.validated_data['contract'].client
            data = {'client': client_id}
            serializer.save(**data)

        else:
            raise ValidationError('User is not support')