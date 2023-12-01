from django.http import JsonResponse
from . models import *

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