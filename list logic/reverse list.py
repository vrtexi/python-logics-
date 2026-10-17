# Q7 — Reverse a list without .reverse()

# Given:

# a = [10, 20, 30, 40, 50]

# Expected:

# [50, 40, 30, 20, 10]

# Don't use .reverse() or slicing [::-1].

a = [10, 20, 30, 40, 50]
num = len(a)
save = 0
for i in range(0,len(a)//2):
  save = a[i]
  a[i] = a[num-1]
  a[num-1] = save
  num -=1
print(a)