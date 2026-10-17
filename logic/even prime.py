# Q6. Print even numbers and tell whether they're prime

# This is the question you just solved:

# Input lower and upper limits. For every number in the range, if it is even, check whether it is prime.
# Try rewriting it from scratch using the found method.

lower = int(input("1: "))
upper = int(input("2: "))

for i in range(lower,upper+1):
  if i % 2== 0:
    found = False
    for n in range(2,i):
      if i % n ==0:
        found = True
    if not found:
      print(i,"Prime")
      
      
