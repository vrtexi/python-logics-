# Write a program to input a lower limit and upper limit and diaplay all prime numbers between such limits 

lower_limit = int(input("enter the lower limit: "))
upper_limit= int(input("enter the upper limit: "))

for i in range(lower_limit,upper_limit+1):
  for n in range(2,i):
    is_prime = True
    if i % n == 0:
      is_prime = False
      break
  if is_prime:
    print(i)

  