# Q6 — Frequency of an element

# Now make the search slightly harder.

# a = [2, 5, 2, 8, 2, 9, 5, 2]
# target = 2

# Find how many times target occurs.

a = [2, 5, 2, 8, 2, 9, 5, 2] 
target = 2
occur_counts = 0
for i  in a:
  if target == i:
    occur_counts += 1
    
print(occur_counts)