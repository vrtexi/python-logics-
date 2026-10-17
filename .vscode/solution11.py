# WAP to input a number and check that such number is prime or not.

number = int(input("Enter your number: "))

# for i in range(2,number):
#    if number % i == 0:
#      print("not a prime")2
#      break
# else:
#   print("prime")


i = 2
while i < number:
  if number % i ==0:
    print("not a prime")
    break
  else:
    i +=1
else:
  print("prime")