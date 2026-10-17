# ⭐ Challenge

# Q9. Find the number with the most divisors

# Input:

# lower = 1
# upper = 20

# For every number:

# Find how many divisors it has.
# Remember which number has the highest count.
# At the end, print that number and its divisor count.

# For example, you'd discover that some numbers have more divisors than others.

# Don't attempt this one yet. Do Q1 → Q4 first.

lower = int(input("1: "))
upper = int(input("2: "))

max_count = 0
max_number = 0

for i in range(lower, upper + 1):

    divisor_count = 0

    for n in range(1, i + 1):

        if i % n == 0:
            divisor_count +=1

    if divisor_count > max_count:
      max_count = divisor_count
      max_number = i
    # kya is number ke divisors ab tak ke maximum se zyada hain?

print(max_count , max_number )