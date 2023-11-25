from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

@csrf_exempt
def startManufacturing(request):
    if request.method=="POST":
        data = json.loads(request.body.decode('utf-8'))
        name=data.get('name')
        quantity=data.get('quantity')
        Manufacturing.objects.create(
            name=name,
            quantity=quantity   
        )
        return HttpResponse()
    
@csrf_exempt
def updateStatus(request):
    if request.method=="POST":
        data = json.loads(request.body.decode('utf-8'))
        id=data.get('id')
        status=data.get('status')
        m=Manufacturing.objects.get(id=id)
        if m.status=="In Process" and status=="Manufactured":
            name=m.name
            product=Inventory.objects.get(name=name)
            product.quantity+=m.quantity
            product.save()
        elif m.status=="Manufactured" and status=="In Process":
            name=m.name
            product=Inventory.objects.get(name=name)
            product.quantity-=m.quantity
            product.save()
        m.status=status
        m.save()
        return HttpResponse()
    
def listManufacturing(request):
    manufacture_db=Manufacturing.objects.all()
    manufacture=dict()
    for m in manufacture_db:
        if m.end_date is not None:
            end_date=m.end_date
        else:
            end_date="-"
        manufacture[m.id]={'name':m.name,
                           'quantity':m.quantity,
                           'end_date':end_date,
                           'status':m.status}
    return JsonResponse(manufacture)    
        