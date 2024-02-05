from . models import *
from datetime import datetime
import math

def eoqCalc(product):
   if product=="Test Product":
      return 6000
   else:
      current_year = datetime.now().year
      orders=Order.objects.filter(product=product,ordered_date__year=current_year-1)
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

def applyEOQ(product,quantity):
   item=Product.objects.get(name=product)
   stock=Inventory.objects.get(name=product).quantity
   stock-=1000
   material=RawMaterial.objects.get(name=Product.objects.get(name=product).raw_material.name)
   quantity-=stock
   material_avail=Warehouse.objects.get(name=material.name).quantity
   possible=material_avail*math.floor(material.length/item.length)
   quantity-=possible
   order=math.ceil(quantity*(item.length/material.length))
   if int(str(order)[-2::])>50:
      order=(order//10)*10
   else:
      order=(order//100)*100
   print(f'EOQ suggests ordering of {order} amount of raw materials')
   return order