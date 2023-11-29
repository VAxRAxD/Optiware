from django.db import models

class Supplier(models.Model):
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    
    def __str__(self):
        return self.name
    
class RawMaterial(models.Model):
    name=models.CharField(max_length=100,null=True)
    thickness=models.FloatField(null=True)
    length=models.FloatField(null=True)
    price=models.IntegerField(null=True)
    supplier=models.ForeignKey(Supplier,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    thickness=models.FloatField(null=True)
    length=models.FloatField(null=True)
    raw_material=models.ForeignKey(RawMaterial,null=True,on_delete=models.SET_NULL)
    price=models.IntegerField(null=True)
    minimum_order=models.IntegerField(default=100,null=True)
    
    def __str__(self):
        return self.name
    
class Warehouse(models.Model):
    name=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    name=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

    
class Customer(models.Model):
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    PAYMENT=(
        ('Paid','Paid'),
        ('Unpaid','Unpaid')
    )
    ORDER=(
        ('Pending', 'Pending'),
        ('Processing','Processing'),
        ('Ready','Ready'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    ordered_date=models.DateField(null=True,blank=True)
    delivered_date=models.DateField(null=True,blank=True)
    amount=models.IntegerField(null=True)
    payment_status=models.CharField(max_length=200, null=True, choices=PAYMENT,default="Unpaid")
    order_status=models.CharField(max_length=200, null=True, choices=ORDER,default="Pending")
    
    def __str__(self):
        return f'{self.ordered_date} : {self.customer} ordered {self.quantity} {self.product}'
    
class Manufacturing(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('In Process','In Process'),
        ('Manufactured','Manufactured')
    )
    name=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    start_date=models.DateTimeField(auto_now_add=True,null=True)
    end_date=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS,default="Pending")
    
    def __str__(self):
        return f"{self.name} {self.start_date}"