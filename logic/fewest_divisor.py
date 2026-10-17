# 🟢 Practice 2 — Find the number with the FEWEST divisors

# Example:

# lower = 1
# upper = 10

# You need to find:

# number = ?
# divisor count = ?

# Same structure as the previous question, but now instead of asking:

# is this count GREATER than max_count?

# you'll need to think:

# "Is this count smaller than the count I've remembered?"

# Don't code yet. Tell me what you think min_count and min_number should initially be.

lower = int(input("1: "))
upper = int(input("2: "))

first = True

for i in range(lower, upper + 1):

    divisor_count = 0

    for n in range(1, i + 1):
        if i % n == 0:
            divisor_count += 1

    if first:
      min_div = divisor_count
      min_number = i
      first = False

    else:
        if divisor_count < min_div:
          min_div = divisor_count
          min_number = i
print(min_div,min_number)
  