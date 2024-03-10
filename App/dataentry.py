import os
from django.http import HttpResponse
from django.conf import settings
from . models import *

#Specify your path of csv file here
file_path = os.path.join(settings.BASE_DIR, 'App/<filename>.csv')

def enterCustomers(request):
    with open(file_path,'r') as f:
        for line in f.readlines():
            name,address,phone,email=line.split(',')
            Customer.objects.create(
                name=name,
                address=address,
                contact=phone,
                email=email
            )
    return HttpResponse()

def enterOrders(request):
    with open(file_path,'r') as f:
        for line in f.readlines():
            customer,product,quantity,ordered,delivered,amount,payment,order_status=line.split(',')
            customer=customer.strip()
            customer=Customer.objects.get(name=customer)
            ordered=ordered.split('-')[2]+"-"+ordered.split('-')[0]+"-"+ordered.split('-')[1]
            delivered=delivered.split('-')[2]+"-"+delivered.split('-')[0]+"-"+delivered.split('-')[1]
            Order.objects.create(
                customer=customer,
                product=product.strip(),
                quantity=quantity,
                ordered_date=ordered,
                delivered_date=delivered,
                amount=amount,
                payment_status=payment,
                order_status=order_status
            )
    return HttpResponse()

def enterPurchase(request):
    with open(file_path,'r') as f:
        for line in f.readlines():
            supplier,product,quantity,ordered,recieved,amount,purchase=line.split(',')
            supplier=supplier.strip()
            supplier=Supplier.objects.get(name=supplier)
            ordered=ordered.split('-')[2]+"-"+ordered.split('-')[0]+"-"+ordered.split('-')[1]
            recieved=recieved.split('-')[2]+"-"+recieved.split('-')[0]+"-"+recieved.split('-')[1]
            Purchase.objects.create(
                supplier=supplier,
                product=product,
                quantity=quantity,
                ordered_date=ordered,
                received_date=recieved,
                amount=amount,
                purchase_status=purchase
            )
    return HttpResponse()

def enterManufacture(request):
    with open(file_path,'r') as f:
        for line in f.readlines():
            product,quantity,order_no,start_date,end_date,status=line.split(",")
            start_date=start_date.split('-')[2]+"-"+start_date.split('-')[0]+"-"+start_date.split('-')[1]
            end_date=end_date.split('-')[2]+"-"+end_date.split('-')[0]+"-"+end_date.split('-')[1]
            Manufacturing.objects.create(
                name=product,
                quantity=quantity,
                status=status,
                start_date=start_date,
                end_date=end_date
            )
    return HttpResponse()