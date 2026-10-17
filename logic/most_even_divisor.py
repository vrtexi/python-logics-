# 🟡 Practice 4 — Number with most even divisors

# For every number:

# Count only the divisors that are even.

# Example:

# 12

# Divisors:

# 1, 2, 3, 4, 6, 12

# Even divisors:

# 2, 4, 6, 12

# Count = 4

# Then find which number in the range has the most even divisors.

lower= int(input("1: "))
upper = int(input("2: "))

for i in range(lower , upper+1):
  divisor = 0
  count1=0
  max_count = 0
  max_number=0
  for n in range(1,i+1):
    if i % n ==0:
      if n % 2 ==0:
        divisor = n 
        count1 +=1
  if divisor > max_count:
    max_count = divisor
    max_number = i
  print(max_number , max_count , count1)
