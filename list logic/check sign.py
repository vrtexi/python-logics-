# Q4 — Count positive, negative and zero

# Try:

# a = [5, -2, 0, 8, -7, 0, 3, -1]

# Expected:

# Positive = 3
# Negative = 3
# Zero = 2

# Do it using a for loop and if/elif/else.

a = [5, -2, 0, 8, -7, 0, 3, -1]
positive_num = 0
negative_num = 0
zeros = 0 
for i in a:
  if i == 0:
    zeros +=1
  elif i < 0:
    negative_num +=1
  else:
    positive_num +=1
print(positive_num,negative_num,zeros)