# Take a number and count how many digits it has.

# 45872 → 5 digits

n= int(input("enter a num: "))
count = 0 
while n>0:
  n = n // 10
  count +=1
print(count)