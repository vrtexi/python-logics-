# 🔴 Level 4 — Actual logic practice

# Q7. Find the first number divisible by both 3 and 5

# Input lower and upper limits.

# Go through the numbers and print the first number that is divisible by both 3 and 5.

# Example:

# Lower = 1
# Upper = 100

# 15
# Once you find it, stop searching.

# This makes you think about:
# break
# and when you should use it.


lower = int(input("1: "))
upper = int(input("2: "))

for i in range(lower, upper+1):
  found = False
  if i % 3 ==0 and i % 5 ==0:
    found = True
    break
if found:
  print(i)