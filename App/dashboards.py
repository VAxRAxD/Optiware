from django.http import JsonResponse
from . models import *
import os
from csv import DictReader

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
    data={
        'customers':100,
        'gross_revenue':100,
        'net_revenue':70,
        'orders':1500,
        'sales':{
            'graph':{
                'Jan-2023':{'orders':50,'sales':4,'profit':2},
                'Feb-2023':{'orders':50,'sales':4,'profit':2},
                'Mar-2023':{'orders':50,'sales':4,'profit':1}
            },
            'orders':150,
            'sales':12,
            'profit':5
        },
        'product':{
            'graph':{
                'Jan-2023':{'debring':3,'caplock':3,'torson':3,'compression_spring':3,'security_metre_wire':3,'ic_lock_cover':3},
                'Feb-2023':{'debring':3,'caplock':3,'torson':3,'compression_spring':3,'security_metre_wire':3,'ic_lock_cover':3},
                'Mar-2023':{'debring':4,'caplock':4,'torson':4,'compression_spring':4,'security_metre_wire':4,'ic_lock_cover':4}
            },
            'debring':10,
            'caplock':10,
            'torson':10,
            'compression_spring':10,
            'security_metre_wire':10,
            'ic_lock_cover':10
        }
    }
    return JsonResponse(data)