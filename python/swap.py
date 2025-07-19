a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(f"Original values: a = {a}, b = {b}")

temp = a 
a = b
b = temp 

print(f"Swaped numbers : a = {a} , b = {b}")