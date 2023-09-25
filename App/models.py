from django.db import models

# class RawMaterials(models.Model):
#     name = models.CharField(max_length=100, unique=True,null=True)
#     description = models.TextField(max_length=200,null=True)
    
#     def __str__(self):
#         return self.name

class Warehouse(models.Model):
    # product = models.CharField(max_length=100, unique=True, null = True)
    # supplier = models.CharField(max_length=100, null = True)
    # employee = models.CharField(max_length=100, null = True)
    # raw_material = models.CharField(max_length=100, null = True)
    
    def __str__(self):
        return "Henriques Shop"

class Product(models.Model):
    name = models.CharField(max_length=100, unique= True,null = True)
    price = models.IntegerField(null = True)
    description = models.TextField(max_length=200, null = True)
    warehouse= models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        default=None
    )
    
    def __str__(self):
        return self.name


# class Transaction(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     type = models.CharField(max_length=100, null = True)


# class Order(models.Model):
#     item = models.CharField(max_length=100, null = True)
#     quantity = models.CharField(max_length=100, null = True)
#     date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=100, null = True)
#     transaction = models.CharField(max_length=100, null = True)

#     def __str__(self):
#         return self.item


class Supplier(models.Model):
    name = models.CharField(max_length=100, null = True)
    #raw_material = models.CharField(max_length=100, null = True)
    warehouse= models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        default=None
    )

    
    def __str__(self):
        return self.name


# class Employee(models.Model):
#     name = models.CharField(max_length=100, null = True)
#     age = models.CharField(max_length=100, null = True)
#     date_of_joining = models.DateField(auto_now_add=True)
#     contact = models.IntegerField(max_length=100, null = True)
#     def __str__(self):
#         return self.name


# class Vehicle(models.Model):
#     name = models.CharField(max_length=100, null = True)
#     type = models.CharField(max_length=100, null = True)
    
#     def __str__(self):
#         return self.name


# class Delivery(models.Model):
    # order = models.CharField(max_length=100, null = True)
    # vehicle = models.CharField(max_length=100, null = True)
    # employee = models.CharField(max_length=100, null = True)
    # location = models.CharField(max_length=100, null = True)

