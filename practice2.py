# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
import os

#write operation
# with open('example.txt', 'w') as file:
#     content=file.write("hello this is write operation")
#     print(content)


#readline
# with open ('example.txt', 'r') as file:
#     content= file.readlines()
#     print(content)


# with open('example.txt', 'w') as file:
#     content= file.writelines('Hello World\n' 'this is second line\n' 'this is third line')
#     print(content)




# while True:
#     print("\n1. Add Contact\n2. View Contacts\n3. Exit")
#     choice = input("Choose: ")
#
#     if choice == '1':
#         name = input("Enter name: ")
#         phone = input("Enter phone: ")
#         with open('contacts.txt', 'a') as file:
#             file.write(name + ',' + phone + '\n')
#         print("Contact added.")
#     elif choice == '2':
#         print("Contacts:")
#         with open('contacts.txt', 'r') as file:
#             for line in file:
#                 print(line)
#     elif choice == '3':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice.")



# try:
#     with open('contact.txt', 'r') as myfile:
#         content = myfile.read()
#         print(content)
#
# except FileNotFoundError:
#     print('File not found')
# except Exception as e:
#     print(e)
#
#
# finally:
#     print("file is searched")



#

with open('data1.json', 'r') as file:
    content=file.read()
    print(content)

with open('data1.json', 'w') as file:
    content=file.writelines("name:dhanushree\n" "usn:123\n")
    print(content)

with open('data1.json', 'a') as file:
    content=file.writelines("city:mysore\n" "language:engilsh\n")
#     print(content)
with open('data1.json', 'r') as file:
    content=file.readlines()
    print(content)


# os.rename('data.json', 'data1.txt')
