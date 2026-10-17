# Take n from the user.
# Calculate:
# 1 + 2 + 3 + ... + n

n = int(input("Enter the value of n: "))
total = 0
for x in range (0,n+1):
  total = total + x
print(total)


# n(n+1)/2 formula 
n = int(input("Enter the value of n: "))
total = n*(n+1)/2
print(total)