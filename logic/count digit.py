# Q22 — Count digits

# Input:

# 58372

# Output:

# 5

# Don't convert it to a string.

num = int(input("enter a number: "))
count1 = 0
while True:
  if num == 0:
    break
  num = num//10
  count1 +=1
print(count1)