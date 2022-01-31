from django.contrib import admin

# Register your models here.

from .models import Customer, BankDetails

admin.site.register(Customer)
admin.site.register(BankDetails)