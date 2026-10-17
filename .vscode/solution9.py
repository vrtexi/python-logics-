# Take a number and reverse it.

# Example:
# 12345 → 54321

a = 54321
# reversed_num = int(str(a)[::-1])
# print(reversed_num)
rev = 0
while a!=0:
  r= a%10
  a = a//10
  rev = rev*10+r
print("reverse is : ", rev)
  
