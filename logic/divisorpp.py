# Q4. Find whether a number has a divisor

# Input a number n.
# Check whether n has any divisor between 2 and n-1.

# Example:

# n = 15

# 15 % 2 → not 0
# 15 % 3 → 0

# Divisor found.
# Use a Boolean found.
# This is basically the prime logic you just learned, but without actually asking whether it's prime.


n = int(input("Enter a number: "))
found = False
for i in range(2,n-1):
  if n % i == 0:
    found = True
    break
if found:
  print("found")
else:
  print("not find")
   
