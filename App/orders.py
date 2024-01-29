from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import *
from . eoq import *
import json, math

def listOrders(request):
    order_db=Order.objects.all()
    order=dict()
    for o in order_db:
        order[o.id]={'customer':o.customer.name,
                     'product':o.product,
                     'quantity':o.quantity,
                     'ordered_date':o.ordered_date,
                     'delivered_date':o.delivered_date,
                     'amount':o.amount,
                     'payment_status':o.payment_status,
                     'order_status':o.order_status}
    return JsonResponse(order)

@csrf_exempt
def placeOrder(request):
    if request.method=="POST":
        data = json.loads(request.body.decode('utf-8'))
        customer=data.get('customer')
        product=data.get('product')
        quantity=data.get('quantity')
        stock=Inventory.objects.get(name=product)
        product=Product.objects.get(name=product)
        material=Warehouse.objects.get(name=product.raw_material.name)
        required=quantity-stock.quantity
        ppp=math.floor(product.raw_material.length/product.length)
        if required<=0:
            print("Order is Ready")
            quantity-=stock.quantity
        elif required<=material.quantity*ppp:
            if required%ppp==0:
                print(f'{required//ppp} rods are being utililsed')
            else:
                print(f'{(required//ppp)+1} rods are being utililsed')
            print("Order under process")
        else:
            required-=material.quantity*ppp
            print(f'{required} units required')
            order=math.ceil(required*(product.length/product.raw_material.length))+100
            order=(order//10)*10
            print(f"Ordering {order} units of raw materials")
    return HttpResponse()