# Q5 — Search for an element

# Now slightly increase the difficulty.

# Given:

# a = [10, 25, 7, 43, 18, 9]
# target = 43

# Find whether target exists in the list without using in().
a = [10, 25, 7, 43, 18, 9]
target = 431
found = False
for i in a:
  if target == i:
    found = True
if found:
  print("Found")
else:
  print("Not founds")
