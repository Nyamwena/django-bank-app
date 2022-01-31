from django.shortcuts import render
from .models import Customer, BankDetails


# Create your views here.

def dashboard(request):
    customers = BankDetails.objects.all()
    context = {'customers': customers}
    return render(request, 'base/index.html', context)


def view_details(request, pk):
    customers = BankDetails.objects.get(customer_id=pk)
    context = {'customers': customers}
    return render(request, 'base/customer_details.html', context)
