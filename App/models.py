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