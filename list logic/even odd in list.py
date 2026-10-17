# Q3: Count how many even and odd numbers are present in a list.

# Example:

# a = [10, 7, 4, 9, 12, 15, 20]

# Expected:

# Even = 4
# Odd = 3

a = [10, 7, 4, 9, 12, 15, 20]
even_count = 0
odd_count = 0
for i in a:
  if i % 2 == 0:
    even_count +=1
  else:
    odd_count +=1
print(even_count,odd_count)