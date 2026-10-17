# 🔴 Practice 5 — Challenge

# Find the number between 1 and 100 that has the largest number of divisors.

# But this time, after finding it, also print:

# Number: ?
# Divisors: ?

# And here's the important part:

# Don't ask me for the code immediately.

# For each problem, send me your attempt—even if it's completely wrong.

# I'll help you trace it like:

# i = ?
# ↓
# divisor_count = ?
# ↓
# n = ?
# ↓
# condition
# ↓
# variable changes

# That's exactly the skill we want to build.


num1 = 1
num2 = 100
max_number=0
max_count = 0
for i in range(num1,num2):
  divisor = 0
  count =0
  for n in range(1,i+1):
    if i %n == 0:
      divisor =n
      count +=1
  if count > max_count:
    max_count = count
    max_number = i
print(max_count, max_number)
    
    
      