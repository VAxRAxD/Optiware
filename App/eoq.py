from . models import *
from datetime import datetime
import math

def eoq(product):
   current_year = datetime.now().year
   orders=Order.objects.filter(product=product,ordered_date__year=current_year-1)
   print(orders)
   d=sum([i.quantity for i in orders])
   s=sum([i.amount for i in orders])/len(orders)
   h={"Debring": 2,
      "Caplock": 1,
      "Torsion Spring": 1.5,
      "Compression Spring": 1,
      "Security Metre Wire": 2,
      "IC Lock Cover": 20
   }
   return round(math.sqrt((2*d*s)/h[product]))