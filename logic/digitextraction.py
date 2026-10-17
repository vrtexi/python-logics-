# Q5 — Extract digits

# Take a 3-digit number and print its:

# Hundreds digit
# Tens digit
# Ones digit

# Example:

# Input: 583

# Hundreds = 5
# Tens = 8
# Ones = 3

# This one is important because it introduces the thinking behind % and //.

n = int(input("enter a number: "))

while n>0:
  r = n%10
  n = n//10
  print(r)
  