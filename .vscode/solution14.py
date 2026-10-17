# wap to input a number and display sum of digits of such numbers
# for eg Enter = 578
# SOD - 5 + 7+ 8= 20

a = int(input("enter a number: "))
sum = 0
while a!=0:
  r = a%10
  a = a//10
  sum +=r
print(sum)