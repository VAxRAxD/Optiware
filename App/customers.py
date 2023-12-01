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

@csrf_exempt
def updateCustomers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name=data.get('name')
        type=data.get('type')
        c=Customer.objects.get(name=name)
        for t in type:
            if t=="email":
                email=data.get('emal')
                c.email=email
            elif t=="address":
                address=data.get('address')
                c.address=address
            else:
                contact=data.get('contact')
                c.contact=contact
        c.save()            
    return HttpResponse()

@csrf_exempt
def addCustomers(request):
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