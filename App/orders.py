from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from . models import *
from . manufacture import *
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
        try:
            customer=Customer.objects.get(name=customer)
        except:
            return HttpResponseBadRequest()
        product=data.get('product')
        quantity=data.get('quantity')
        stock=Inventory.objects.get(name=product)
        product=Product.objects.get(name=product)
        material=Warehouse.objects.get(name=product.raw_material.name)
        required=quantity-stock.quantity
        ppp=math.floor(product.raw_material.length/product.length)
        demand=0
        Order.objects.create(
            customer=customer,
            product=product.name,
            quantity=quantity,
            amount=product.price*quantity,
        )
        if required<=0:
            print("Order is Ready")
            stock.quantity-=quantity
            stock.save()
        elif required<=material.quantity*ppp:
            stock.quantity=0
            stock.save()
            Manufacturing.objects.create(
                name=product,
                quantity=required  
            )
            if required%ppp==0:
                print(f'{required//ppp} rods are being utililsed')
                material.quantity-=required//ppp
                material.save()
            else:
                print(f'{(required//ppp)+1} rods are being utililsed')
                material.quantity-=(required//ppp)+1
                material.save()
            print("Order under process")
        else:
            stock.quantity=0
            stock.save()
            required-=material.quantity*ppp
            print(f'{required} units required')
            Manufacturing.objects.create(
                name=product,
                quantity=material.quantity*ppp  
            )
            material.quantity=0
            material.save()
            order=math.ceil(required*(product.length/product.raw_material.length))
            order=((order+9)//10)*10
            demand+=order
            print(f"{order} needs to be ordered to complete order")
        eoq_=eoqCalc(product.name)
        demand+=applyEOQ(product, eoq_)
        if demand>=0:
            print(f"Ordering {demand} units of raw materials")
        Purchase.objects.create(
            supplier=product.raw_material.supplier,
            product=product.raw_material.name,
            quantity=demand,
            amount=demand*(product.raw_material.price)
        )
    return HttpResponse()