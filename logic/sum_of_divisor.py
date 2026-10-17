# For every number from lower to upper, calculate the sum of its divisors.

# Example:

# 6

# Divisors:

# 1, 2, 3, 6

# So:

# 1 + 2 + 3 + 6 = 12

# Your program should determine which number has the largest sum of divisors.

# This is a very good practice because you're changing:

# divisor_count += 1

# into a different kind of accumulator.

lower = int(input("1: "))
upper = int(input("2: "))

for i in range(lower,upper+1):
  divisor=0
  sum1=0
  for n in range(1,i+1):
    if i%n ==0:
      divisors = n
      sum1 = sum1 +divisors
  print(divisors, n , sum1)