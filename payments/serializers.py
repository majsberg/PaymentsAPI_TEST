from rest_framework import serializers
from payments.models import Apartment, Contract, Payment
from django.contrib.auth.models import User


class ApartmentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apartment
        fields = "__all__"


class ContractsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class PaymentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UsersModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = '__all__'
