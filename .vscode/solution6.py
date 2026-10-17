#WAP to input limit and upper limit and isplay all numbers divisible by 5 between such limit 

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

# for x in range(lower_limit,upper_limit+1):
#   if x %5== 0:
#     print(x)
    
current = lower_limit
while current <= upper_limit:
  if current % 5==0:
    print(current)
  current +=1
    