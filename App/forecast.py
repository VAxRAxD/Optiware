from django.http import JsonResponse
from . models import *

def getForecast(request):
    sales=[288313, 315088, 296631, 278373, 291015, 306766, 313720, 276616, 314080, 305260, 319010, 296734]
    purchase=[288313, 315088, 296631, 278373, 291015, 306766, 313720, 276616, 314080, 305260, 319010, 296734]
    demand={
        'Debring':[32670 for _ in range(10)],
        'Caplock':[32670 for _ in range(10)],
        'Torsion Spring':[32670 for _ in range(10)],
        'Compression Spring':[32670 for _ in range(10)],
        'Security Metre Wire':[32670 for _ in range(10)],
        'IC Lock Cover':[32670 for _ in range(10)]
    }
    forecast=dict()
    forecast['sales']=sales
    forecast['purchase']=purchase
    forecast['demand']=demand
    return JsonResponse(forecast)