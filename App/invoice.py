from django.http import JsonResponse
from . models import *

def getInvoiceData(request,id):
    return