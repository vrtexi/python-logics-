# WAP TO INPUT a lower limit and upper limit and display all Palindrome number lies between such limit.

lower_limit = int(input("enter the lower_limit: "))
upper_limit = int(input("Enter the upper limit: "))



for n in range(lower_limit,upper_limit+1):
  temp = n
  rev = 0
  while temp!=0:
      r = temp%10
      temp = temp//10
      rev = rev*10+r
  if rev == n:
    print(n)
