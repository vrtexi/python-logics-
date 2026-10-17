# Q8. Count numbers having a divisor

# Input lower and upper.

# For every number, check whether it has a divisor between 2 and number - 1.

# Count how many numbers have at least one divisor.

# Example:

# 10 → 20

# You don't need to print the divisors. Just give the final count.

# This is excellent practice for your found = False → True idea.

lower = int(input("1: "))
upper = int(input("2: "))
count = 0
for i in range(lower,upper+1):
  found = False
  for n in range(2,i):
    if i % n == 0:
      found = True
      count +=1
if found:
  print(count)