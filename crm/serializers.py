from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Client, Contract, Event


class Registerializer(serializers.ModelSerializer):
    group = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'group']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ['id']
        extra_kwargs = {'sales_contact': {'required': False}}


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ['id', 'date_created', 'date_updated', 'contract']
        extra_kwargs = {'sales_contact': {'required': False}}


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['id', 'date_created', 'date_updated', 'client']