from django.shortcuts import render
from .models import Customer

def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customers/profile.html', {'customer': customer})
