from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Apartment, Contract, Payment


# Register your models here.
admin.site.register(Apartment)
admin.site.register(Contract)
admin.site.register(Payment)