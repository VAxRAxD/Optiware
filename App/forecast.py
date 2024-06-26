from django.http import JsonResponse
from . models import *

def getForecast(request):
    sales=[288313, 315088, 296631, 278373, 291015, 306766, 313720, 276616, 314080, 305260, 319010, 296734]
    purchase=[288313, 315088, 296631, 278373, 291015, 306766, 313720, 276616, 314080, 305260, 319010, 296734]
    demand={
        'Debring':[19645, 9137, 20200, 22265, 8293, 18168, 14523, 12792, 9664, 23262, 10355, 20799],
        'Caplock':[12174, 10446, 18990, 10976, 6680, 11519, 18229, 11180, 6019, 10565, 17746, 10500],
        'Torsion Spring':[36446, 36725,	43361,	35745,	40547, 55286,	27731, 27252,	77578,	21626, 37431,	27901],
        'Compression Spring': [32671, 36837, 29092, 12827, 33294, 24502, 16554, 31042, 16417, 29521, 39914, 29208],
        'Security Metre Wire':[9286, 2513, 4687, 11603, 15734, 5274, 577, 5083, 12251, 2662, 5598, 6894],
        'IC Lock Cover':[414, 185, 349, 407, 322, 27, 365, 533, 402, 685, 500, 586]
    }
    forecast=dict()
    forecast['sales']=sales
    forecast['purchase']=purchase
    forecast['demand']=demand
    return JsonResponse(forecast)