# 🟡 Level 2 — Same idea, slightly harder

# Q3. Count even numbers
# Input lower and upper limits and count how many even numbers exist between them.

# Example:
# 10 → 20

# Even numbers = 6

# Don't just print them. Your program should count them.

lower = int(input("1: "))
upper = int(input("2: "))
count = 0
for i in range(lower, upper+1):
  if i % 2 == 0:
    count +=1
    
print(count)