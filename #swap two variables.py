#swap two variables
a = 5
b = 10
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
#or
x = 15
y = 35
x = x + y   
y = x - y  
x = x - y 
print("Value of x:", x)
print("Value of y:", y)
#or
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
print(f"Original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"Swapped values: a = {a}, b = {b}")