# Q21 — Sum of digits

# Input:

# 583

# Output:

# 16

# Because:

# 5 + 8 + 3 = 16

# Use % 10 and // 10.

num = int(input("enter a number: "))
sum1=0
while True:
  r = num % 10
  num = num//10
  sum1 +=r
  if num ==0:
    break
print(sum1)