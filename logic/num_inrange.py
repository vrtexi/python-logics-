# 🟢 Level 1 — Boolean + loop

# Q1. Find whether a number exists in a range

# Input lower and upper, then input x.
# Check whether x exists between lower and upper.

# Example:
            # Lower: 10
            # Upper: 20
            # x: 15

# 15 exists in the range.

# Hint: You can use a Boolean variable like found.

lower = int(input("1: "))
upper = int(input("2: "))

between1_2 = int(input("A number that should or not be in 1,2: "))
found = False
for i in range(lower,upper +1):
  if between1_2 == i:
    found = True
if found:
  print("Its in between")
else:
  print("not between")