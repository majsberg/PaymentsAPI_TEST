from django.urls import include, path
from .views import ApartmentViewSet, ContractViewSet, PaymentViewSet, UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'apartments', ApartmentViewSet, basename='apartments')
router.register(r'contracts', ContractViewSet, basename='contracts')
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    # ...
    path('', include(router.urls)),
]