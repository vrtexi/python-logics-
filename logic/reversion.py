# Q23 — Reverse a number

# Input:

# 12345

# Output:

# 54321

# Again, use mathematical digit extraction.

num = int(input("Enter a number: "))

while True:
  if num ==0:
    break
  r = num %10
  num = num //10
  print(r, end='')