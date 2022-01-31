from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id_number = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=18)
    address = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class BankDetails(models.Model):
    account_number = models.CharField(max_length=30, unique=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=30)
    branch_code = models.IntegerField()

    def __str__(self):
        return self.account_number
