# python compound interest calculator 
import math
principle = 0 
rate = 0
time = 0

while principle <=0:
  principle = float(input("Enter the principle amount: "))
  if principle <= 0:
    print("Principle can not be less than or equal to 0")


while rate <=0:
  rate = float(input("Enter your rate "))
  if rate<=0:
    print("Rate can not be less or equal to 0")

while time <=0:
  time = float(input("Enter your time "))
  if time<=0:
    print("Time can not be less or equal to 0")  
  
A = principle * pow((1+ rate/100),time)

print(A)
