from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import *

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