# 🟠 Level 3 — Nested loops

# Q5. Check prime numbers in a range

# Input lower and upper limits.

# Print only the prime numbers.

# Example:

# Lower = 10
# Upper = 20

# 11
# 13
# 17
# 19

# This is basically the prime problem you've already practiced, so try doing it without looking at your previous code.

lower = int(input("Input the lower range: "))
upper = int(input("Input the upper range: "))

for i in range(lower,upper + 1):
  found = False
  for n in range(2,i-2):
    if i % n == 0:
      found = True
  if not found:
    print(i)
    