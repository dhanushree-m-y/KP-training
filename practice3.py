# i=1
# for j in range(1,12):
#     print(i)
#     i=i+1
# from operator import index
# from Practice2 import products

# print sum of n numbers

# num= int(input("enter number"))
# numbers = []
# for i in range(0,num):
#      i=i+1
#      numbers.append(i)
#      print(numbers)
# total = sum(numbers)
# print(total)

# rows = 3
# for i in range(1, rows + 1):
#     spaces = rows - i
#     stars = 2*i-1
#     print(' ' * spaces + '*' * stars)

# rows=5
# for i in range(1,rows+1):
#     stars = 1*i
#     print('*' * stars)

# # enumeration
# colors = ["red", "blue", "green", "yellow"]
# for index,color in enumerate(colors, start=1):
#     print(index,color)




# fruits =["apple", "banana", "cherry","cherry"]
# colors = ["red", "green", "blue", "yellow","yellow"]
#
# combinedlist=(fruits+colors)
# newlist=set(combinedlist)
# print(newlist)


# fruits = ['apple','banana','orange',(1,2,3,3)]
# newlist= set(fruits)
# print(newlist)



#10 natural number using while loop
# N=10
# while N>0:
#      print(N)
#      N=N-1



# print sales graetr than 100
# sales=[20,40,60,80,100,150,200,300]
# # for sale in sales:
# #     if sale>=100:
# #         print(f"{sale} sale is greater than 100")
#
#
# # other method using comprehension
# order = [sales for sales in sales if sales>100]
# print(order)


# numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# evennum= []
# oddnum = []
# for i in numlist:
#     if i % 2 == 0:
#         print(i)
#         evennum.append(i)
#     else:
#         oddnum.append(i)
#     print(evennum,oddnum)



# # loggers
# import logging
#
#
# logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
#
# # Create a list
# fruits = ["apple", "banana", "cherry"]
# logging.warning("Initial list: %s", fruits)
#
# # Add an item
# fruits.append("orange")
# logging.info("Added 'orange': %s", fruits)
#
# # Remove an item
# fruits.remove("banana")
# logging.info("Removed 'banana': %s", fruits)
#
# # Sort the list
# fruits.sort()
# logging.info("Sorted list: %s", fruits)
#
# # Final output
# print("Final fruit list:", fruits)

# list1 = str(input("Enter the length"))
# list1=[]
# for i in range(list1):
#     list.append(int(input("Enter a number ")))
# print(list1)


# strings
#
# str1='dhanushree'
# str2='ullaskumar'
# # print(str1, str2)
# # print(str1[0:8])
# # print(str1[-3:])
# print(str1[2:]) #prints 1st two letters
# print(str1[:2]) #prints without first two letters
# print(str1[-2:])#prints last two letters

# print(str1[::-1])
# # print("updated string" ,str1[:6] + str2)
# print(str1[-1:-5])



# update str
# print(str1.upper())
# print(str2.replace('d','h'))




# str='welcome back {}'
# print(str.format('Suman'))


# n natural number
# n=int(input("enter the number"))
# for i in range(1, n+1):
#     print(i, end=" ")

# odd and even
# num =int(input("enetr a number"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

#
# strinput = input("enetr the input")
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# for vowel in vowels:
#     if vowel in strinput:
#         count = strinput.count(vowel)
#         print(count)
#

# print("number of consonents:",consonent_count)


# Book={ "Title": "Python Mastery",
# "Author": "John Doe",
# "Year": 2023,
#  "Pages": 450,
# "Available": True
# }
#
# print(Book)
# print(f"The book '{Book['Title']}' has {Book['Pages']} pages.")








# #simple shopping cart sysytem
# products = []
# cart=[]
#
# def add_product(name,price):
#     price=float(price)
#     products.append({"name":name,"price":price})
#
# def view_product():
#     for product in products:
#         print({"name":product["name"],"price":product["price"]})
#
# def add_to_cart(name,quantity):
#     cart.append({"name": name, "quantity": quantity})
#
# def view_cart():
#     for item in cart:
#         print({"item":item["name"],"quantity":item["quantity"]})
#
#
# def print_bill():
#     total = 0
#     for item in cart:
#         for product in products:
#             if product["name"]==item["name"]:
#                 amount= product["price"]* item["quantity"]
#                 print(item["name"],"x",item["quantity"],"=",amount)
#                 total=total+amount
#     print("total:",total)
#
# add_product("cherry",56)
# view_product()
#
# while True:
#     print("Menu")
#     print("1.Add product")
#     print("2.View product")
#     print("3.add to cart")
#     print("4.View cart")
#     print("5.generate bill")
#     print("6.Exit")
#
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         name= input("Enter product name: ")
#         price=input("Enter product price: ")
#         add_product(name,price)
#     elif choice=="2":
#         view_product()
#     elif choice=="3":
#         name=input("Enter product name: ")
#         quantity=int(input("Enter product quantity: "))
#         add_to_cart(name,quantity)
#     elif choice =="4":
#         view_cart()
#     elif choice =="5":
#         print_bill()
#     else:
#         print("Thank you")
#         break



#arrays
# memory allocation: 1000,1000+4,1000+8
#
# def array_sum(arr):
#     total = 0
#     for num in arr:
#         total += num
#     return total
# arr = [1, 2, 3, 4, 5]
# print(array_sum(arr))

print("hello")





