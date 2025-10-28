#simple shopping cart sysytem

"""You start with an empty list of products and an empty shopping cart.

You can add products with a name and price.

You can see all the products you've added.

You can add products to your shopping cart with a specified quantity.

You can view what's in your cart.

When you want to buy everything, the program calculates the total price by matching each item in the cart to its product price.

You can keep adding, removing, or viewing items, and then finally generate the bill to see how much you need to pay.

The program keeps running until you choose to exit."""



products = []
cart=[]

def add_product(name,price):
    price=float(price)
    products.append({"name":name,"price":price})

def view_product():
    for product in products:
        print({"name":product["name"],"price":product["price"]})

def add_to_cart(name,quantity):
    cart.append({"name": name, "quantity": quantity})

def view_cart():
    for item in cart:
        print({"item":item["name"],"quantity":item["quantity"]})


def print_bill():
    total = 0
    for item in cart:
        for product in products:
            if product["name"]==item["name"]:
                amount= product["price"]* item["quantity"]
                print(item["name"],"x",item["quantity"],"=",amount)
                total=total+amount
    print("total:",total)

add_product("cherry",56)
view_product()

while True:
    print("Menu")
    print("1.Add product")
    print("2.View product")
    print("3.add to cart")
    print("4.View cart")
    print("5.generate bill")
    print("6.Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name= input("Enter product name: ")
        price=input("Enter product price: ")
        add_product(name,price)
    elif choice=="2":
        view_product()
    elif choice=="3":
        name=input("Enter product name: ")
        quantity=int(input("Enter product quantity: "))
        add_to_cart(name,quantity)
    elif choice =="4":
        view_cart()
    elif choice =="5":
        print_bill()
    else:
        print("Thank you")
        break