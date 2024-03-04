from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import *
import json, math

def listPurchase(request):
    purchase_db=Purchase.objects.all()
    purchases=dict()
    for p in purchase_db:
        purchases[p.id]={'supplier':p.supplier.name,
                     'product':p.product,
                     'quantity':p.quantity,
                     'ordered_date':p.ordered_date,
                     'received_date':p.received_date,
                     'amount':p.amount,
                     'purchase_status':p.purchase_status}
    return JsonResponse(purchases)

@csrf_exempt
def purchaseRawMaterial(request):
    if request.method=="POST":
        data = json.loads(request.body.decode('utf-8'))
        supplier=data.get('supplier')
        product=data.get('product')
        quantity=data.get('quantity')
        amount=quantity*(RawMaterial.objects.get(name=product).price)
        Purchase.objects.create(
            supplier=supplier,
            product=product,
            quantity=quantity,
            amount=amount
            
        )
        print(f'Ordered {quantity} {product} from {supplier}')
        return HttpResponse()