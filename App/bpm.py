from databases import *

stock=stock
raw_material=raw_material
suppliers=suppliers
customers=customers
orders=orders

def placeorder():
    global customers, orders
    name=input("Enter your name: ") 
    if name not in customers:
        print("\nYou seem to be a new customer. Please register")
        registerCustomer(name)
    cart=list()
    products=list(stock.keys())
    print("Please place your order:")
    print("Press 1 for Spring 1\nPress 2 for Spring 2\nPress 3 for Spring 3\nPress 0 to exit menu")
    while True:
        choice=int(input(("\nEnter the Spring type you want to order: ")))
        if choice==0 :
            break
        elif choice in [1,2,3]:
            quant=int(input("Enter the quantity of springs you want to order: "))
            cart.append([products[choice-1],quant])
        else:
            print("Please Enter a valid choice\n")
            continue
    if confirmOrder():
        print("Your ordered has been confirmed successfully!!")
        addr=getShippingAddress(name)
        ord_no=len(orders)
        orders[ord_no]={
            "customer":name,
            "shipping_addr":addr,
            "products":[items[0] for items in cart],
            "ind_status":[0 for _ in range(len(cart))],
            "ovr_status":"Under Process"
        }
    else:
        pass
    for i in range(len(cart)):
        while not checkStock(cart[i][0],cart[i][1]):
            if not checkRawMaterials(cart[i][0],cart[i][1]):
                requestRawMaterials(cart[i][0],cart[i][1])
            manufacture(cart[i][0],cart[i][1])
        retrieveProduct(cart[i][0],cart[i][1])
        orders[ord_no]['ind_status'][i]=1

def registerCustomer(name):
    global customers
    addr=input("Enter your address: ")
    customers[name]={"address":addr}
    print("\nRegistered Successfully! You can Now place your order\n")
    
def checkStock(spring,quant):
    if quant<=stock[spring]['quantity']:
        print(f"\n{spring} available in inventory")
        return True
    else:
        quant -= stock[spring]['quantity']
        print(f"\nNot sufficient stock of {spring}")
        return False

def retrieveProduct(spring,quant):
    print(f"\nRetrieving {spring}")
    stock[spring]['quantity'] -= quant
    print(f"\n{spring} retrieved successfully")
    
def manufacture(spring,quant):
    global raw_material
    rm = stock[spring]['raw-material']
    print(f"\nManufacturing {spring}")
    raw_material[rm]['quantity']-=quant
    stock[spring]['quantity']+=quant
    print(f"\n{spring} manufacturing complete")

def checkRawMaterials(spring,quant):
    global raw_material
    print(f"\nChecking for raw materials to manufacture {spring}")
    rm = stock[spring]['raw-material']
    if quant<=raw_material[rm]['quantity']:
        print(f"\nSufficient raw materials available")
        return True
    else:
        print("\nNo sufficient raw materials.Requesting raw materials from Supplier")
        return False

def requestRawMaterials(spring,quant):
    global raw_material
    rm = stock[spring]['raw-material']
    raw_material[rm]['quantity']+=quant
    print("\nRaw materials acquired from Supplier")

def confirmOrder():
    while True:
        confirm = input("\nWould you like to confirm your order? (y/n): ")
        if confirm=='y':
            return True
        elif confirm=='n':
            return False
        else:
            print("Invalid input")

def getShippingAddress(name):
    global customers
    if name in customers:
        return customers[name]['address']

placeorder()    