from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import *

def listCustomers(request):
    customer_db=Customer.objects.all()
    customers=dict()
    for c in customer_db:
        customers[c.id]={'name':c.name,
                         'address':c.address,
                         'contact':c.contact,
                         'email':c.email}
    return JsonResponse(customers)

def updateCustomers(request):
    customer_db=Customer.objects.all()
    customers=dict()
    # cust=Customer.objects.get(pk=id)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name=data.get('name')
        address=data.get('address')
        contact=data.get('contact')
        email=data.get('email')
        Customer.objects.update(
            name=name,
            address=address,
            contact=contact,
            email=email, 
        )
    return HttpResponse(customers)

@csrf_exempt
def customers(request):
    if request.method=="POST":
        data = json.loads(request.body.decode('utf-8'))
        name=data.get('name')
        address=data.get('address')
        contact=data.get('contact')
        email=data.get('email')
        Customer.objects.create(
            name=name,
            address=address,
            contact=contact,
            email=email, 
        )
        return HttpResponse()