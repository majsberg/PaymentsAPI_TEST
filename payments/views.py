from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Apartment, Contract, Payment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .permission import CustomPermission

from .serializers import (ApartmentModelSerializer, ContractsModelSerializer, PaymentsModelSerializer,
                          UsersModelSerializer)


# Create your views here.
class ApartmentViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Apartment.objects.filter(user=user)

    serializer_class = ApartmentModelSerializer
    permission_classes = (IsAuthenticated, )


class ContractViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(apartment__user=user).select_related('apartment')

    serializer_class = ContractsModelSerializer
    permission_classes = (IsAuthenticated, )


class PaymentViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Payment.objects.select_related('contract').filter(contract__apartment__user=user)

    serializer_class = PaymentsModelSerializer
    permission_classes = (IsAuthenticated,)


class UsersViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)

    def create(self, request, *args, **kwargs):
        user_data = self.serializer_class(data=request.data)
        # print(f'user_data: {user_data}')
        hashed_pass = make_password(password=user_data.initial_data['password'],)
        # QueryDict нужен для отправки POST-запроса на регистрацию пользователя через форму DRF
        # new_data = QueryDict.copy(user_data.initial_data)
        new_data = user_data.initial_data
        # print(f'new_data: {new_data}')
        new_data['password'] = hashed_pass
        user_new_data = self.serializer_class(data=new_data)
        # print(f'user_new_data: {user_new_data}')
        user_new_data.is_valid(raise_exception=True)
        self.perform_create(user_new_data)
        headers = self.get_success_headers(user_new_data.data)
        return Response(user_new_data.data, status=status.HTTP_201_CREATED, headers=headers)

    serializer_class = UsersModelSerializer
    permission_classes = (CustomPermission,)

