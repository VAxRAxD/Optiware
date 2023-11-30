from django.http import JsonResponse
from . models import *
import calendar
from datetime import datetime

def store(request):
    product_db=Product.objects.all()
    product=dict()
    for p in product_db:
        product[p.name]={'thickness':p.thickness,
                         'lenght':p.length,
                         'raw_material':p.raw_material.name,
                         'price':p.price}
    raw_material_db=RawMaterial.objects.all()
    raw_material=dict()
    for r in raw_material_db:
        raw_material[r.name]={'thickness':r.thickness,
                         'lenght':r.length,
                         'price':r.price,
                         'supplier':r.supplier.name}
    supplier_db=Supplier.objects.all()
    supplier=dict()
    for s in supplier_db:
        supplier[s.name]={'address':s.address,
                          'contact':s.contact,
                          'email':s.email}
    data=dict()
    data['products']=product
    data['raw_materials']=raw_material
    data['suppliers']=supplier
    return JsonResponse(data)

def inventory(request):
    inventory_db=Inventory.objects.all()
    inventory=dict()
    for p in inventory_db:
        inventory[p.name]=p.quantity
    return JsonResponse(inventory)

def dashboard(request):
    current_month=datetime.now().month-1
    current_year=datetime.now().year
    last_3_months=list()
    for _ in range(3):
        if current_month==0:
            current_month=12
            current_year-=1
            last_3_months.append([current_month,current_year])
            current_month-=1
        else:
            last_3_months.append([current_month,current_year])
            current_month-=1
    sales_graph=dict()
    product_graph=dict()
    last_3_months_orders=0
    last_3_months_sales=0
    last_3_months_purchases=0
    debring,caplock,torsion,comprspr,secmw,iclockcover=0,0,0,0,0,0
    for i in range(2,-1,-1):
        records=Order.objects.filter(ordered_date__month=last_3_months[i][0],ordered_date__year=last_3_months[i][1])
        purchase=Purchase.objects.filter(ordered_date__month=last_3_months[i][0],received_date__year=last_3_months[i][1])
        sales=records.aggregate(total_sum=models.Sum('amount'))['total_sum']
        profit=purchase.aggregate(total_sum=models.Sum('amount'))['total_sum']
        debring+=len(records.filter(product="Debring"))
        caplock+=len(records.filter(product="Caplock"))
        torsion+=len(records.filter(product="Torsion Spring"))
        comprspr+=len(records.filter(product="Compression Spring"))
        secmw+=len(records.filter(product="Security Metre Wire"))
        iclockcover+=len(records.filter(product="IC Lock Cover"))
        last_3_months_orders+=len(records)
        last_3_months_sales+=sales
        last_3_months_purchases+=profit
        sales_graph[f'{calendar.month_name[last_3_months[i][0]][:3]}-{last_3_months[i][1]}']={'orders':len(records),'sales':sales,'profit':profit}
        product_graph[f'{calendar.month_name[last_3_months[i][0]][:3]}-{last_3_months[i][1]}']={'debring':len(records.filter(product="Debring")),
                                                                                                'caplock':len(records.filter(product="Caplock")),
                                                                                                'torsion_spring':len(records.filter(product="Torsion Spring")),
                                                                                                'compression_spring':len(records.filter(product="Compression Spring")),
                                                                                                'security_metre_wire':len(records.filter(product="Security Metre Wire")),
                                                                                                'ic_lock_cover':len(records.filter(product="IC Lock Cover"))
                                                                                            }
    data={
        'customers':len(Customer.objects.all()),
        'gross_revenue':Order.objects.aggregate(total_sum=models.Sum('amount'))['total_sum'],
        'net_revenue':(Order.objects.aggregate(total_sum=models.Sum('amount'))['total_sum'])-(Purchase.objects.aggregate(total_sum=models.Sum('amount'))['total_sum']),
        'orders':len(Order.objects.all()),
        'sales':{
            'graph':sales_graph,
            'orders':last_3_months_orders,
            'sales':last_3_months_sales,
            'profit':last_3_months_purchases
        },
        'product':{
            'graph':product_graph,
            'debring':debring,
            'caplock':caplock,
            'torsion_spring':torsion,
            'compression_spring':comprspr,
            'security_metre_wire':secmw,
            'ic_lock_cover':iclockcover
        }
    }
    return JsonResponse(data)