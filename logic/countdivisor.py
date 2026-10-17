# count divisor

lower = int(input("1: "))
upper = int(input("2: "))

for i in range(lower,upper+1):
  
  divisor_count = 0
  
  for n in range(1,i+1):
    if i % n ==0:
      divisor_count +=1
      num = i
  
  print(num, divisor_count)
  