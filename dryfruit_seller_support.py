def viewProduct():
    item = input('Enter product name: ')
    print(products.get(item,'No such product'))
    
def add_Update_Product():
    item1 = input('Enter product name: ')
    price = int(input('Enter price of product: '))
    products.update({item1:price})

def buyProduct():
    global cart,bill
    while(True):
            item2 = input('Enter your product name (-1 to exit): ')
            if(item2 == '-1'):
                break
            while(item2 not in products):
                item2 = input('Enter your product name: ')
            amount=float(input('Enter amount in kg:'))
            bill+=products[item2]*amount
            cart[item2]=cart.get(item2,0)+amount

## Main Program
products = {'walnuts': 1500, 'cashew': 1800, 'almond': 2000, 'pine nuts': 8000}
print("===== Dry-Fruits Seller Support =====")
print("1.Product Rate")
print("2.Updation of Product or Rate")
print("3.Customer Bill")
print("4.Exit the Program")
bill=0
cart={}
while(True):
    op=int(input("Enter (1/2/3/4) :"))
    if(op not in range(1,5)):
        print('Invalid entery')
        continue
    if(op==1):
        viewProduct()
    elif(op==2):
        add_Update_Product()     
    elif(op==3):
       buyProduct()
    else:
        print('Thanks')
        break    
if(len(cart)>0):
        print(f'Your total bill is: {bill} ')
        print('Your purchased products: ')
        for k,v in cart.items():
            print(f'{k} : {v}')           
          
   
    
        
                    

