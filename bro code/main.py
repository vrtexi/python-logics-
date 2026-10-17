# print("hi")
# print("hi world hello kesso hi")
# print('it\'s going to raind today')
# name =input("enter your name ")
# print(name)

# name = input("enter your name: ")
# print("Hello, ", name)  # prints out "Hello, John" if the user enters "John"  23
# print(type(name))
# age = int(input("enter your age: "))
# print("you're ", age, "years old", name)  # prints out "you're 25 years old" if
# exp = eval("2*4+345*4")
# print(exp)

# print( """ aman pandey 
#       22
#       inderpuri new delhi""")

# WRITE A PROGRAM TO SWAP USING 3 DIFF METHODS
# 1. using third variable
# a= 45
# b =54
# c=a
# a=b
# b=c 
# print (a,b)

# #2. using tuple packing and unpacking
# a = 45
# b = 54
# a,b =b,a
# print (a,b)

# #3. using arthematic operators
# a= 45
# b = 54
# a = a+b
# b = a-b
# a=a-b
# print (a,b)

#Write a Program To Convert Float Into Integer
# a=45.6
# print(int(a))  # prints 45

# # 2. Write a Program To Convert Integer Into Float
# a=45
# b= float(a)
# print(b)  # prints 45.0

#Take Different Types Of Data From User And Print Them
# name= input("Enter Your Name: ")
# age = int(input("Enter Your Age: "))
# idnum = int(input("Enter Your Id Num: "))
# print("Name: ", name, "\nAge: ", age, "\nidnum: ", idnum)

# Try this:
# x = ""
# print(x or "Default")  # ??

# y = []
# print(y and "Hi")      # ??

# # Compare:
# a = [1]
# b = [1]
# print(a == b)          # True
# print(a is b)          # False

# Exercise 2: SHOPPING CART PROGRAM 
# item = input("What item would you like to buy? : ")
# price = float(input("What is the price of the item? : "))
# quantity = int(input("How many would you like to buy? :"))
# total = quantity * price

# print(f"Your total would be {total}rs")

# x =  3.14
# y = 4
# z = 5
# result = round(x)
# result = abs(y) ##How far it is from 0
# result = pow(y, 4)
# result = min(x,y,z)
# result = max(x,y,z)
# print(result)

import math 
# print(math.pi)
# print(math.e) 

# result = math.sqrt(9) #3
# result = math.ceil(9.7) #10
# result = math.floor(9.9) #9
# print(result)

#EXERCISE 3 FIND CIRCUMFERENCE OF THE CIRCLE
# C= 2*PI*R
# radius = int(input("Whats the radius of this circle? :"))
# circumference = 2* math.pi * radius
# print(f"Your circumference fo this ciercle is : {round(circumference,2)}")

#EXERCISE 4 AREA OF CIRCLE
# A = PI * R(SQUARE)
# radius = int(input("Whats the radium of ur circle? :"))
# Area = math.pi * pow(radius, 2)
# print(Area)

#EXERCISE 5 HIPOTANEUS OF RIGHT ANGLE TRIANGLE
# H = UNDERROOT OF (a sqr + b sqr)

# a = float(input("Enter your side A : "))
# b = float(input("Enter your side B : "))

# H = math.sqrt(math.pow(a,2) + math.pow(b,2))
# print (H)

# age = int(input("Enter your age : "))

# if age >  18 and age < 99:
#   print("Your are eligible")
# elif age > 100:
#   print("Your are not dead ")
  
# else:
#   print("Your not eligible")

# Ternary operator

# FORMULA = X if condition else Y

# num = 6 
# a = 10
# b = 20
# age = 19
# min = a if b > a else b
# max = a if a>b else b
# status = "Adult" if age>25 else "Teenager"
# print(status)
# print("Positive" if num>0 else "Negative")


