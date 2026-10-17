# Write down User Defined functions of following
# 1.  Factorial of a number (Done)
# 2.  Fibonacci Series (nth term / full series) (done)
# 3.  Sum of N natural numbers (done)
# 4.  Product of N natural numbers
# 5.  Print numbers from 1 to N and N to 1
# 6.  Sum of digits of a number
# 7.  Count digits of a number
# 8.  Reverse a number
# 9.  Power of a number (x^n)
# 10. Check if a number is palindrome

# Medium Level:
# 11. GCD of two numbers (Euclid's algorithm)
# 12. LCM of two numbers using recursion
# 13. Check if String is palindrome or not
# 14. Reverse a String using recursion
# 15. Count vowels / consonants in a string
# 16. Find maximum and minimum in an array
# 17. Sum of List elements


# def fact(n):
#   for i in range(1,n):
#     n = n * i
#   print(n)
# fact(4)

# def factorial(n):
#   if n == 1:
#     return 1
#   return n * factorial(n-1)

# print(factorial(5))

#question 2
# def fabonaci(n):
#   a=0
#   b=1
#   for i in range(1,n+1):
#     print (a,b ) 
#     c = a +b
#     a = b
#     print(c)
# fabonaci(7)

# q3 normal function 
# def sum(n):
#   sumnum =0
#   for i in range(n+1):
#     sumnum = sumnum + i
#   print(sumnum)

# sum(5)

# question 3 using recursion
# def sum(n):
#   if n == 0:
#     return 0
#   return n + sum(n-1)
# print(sum(5))

# question 4 
# def product(n):
#   productnum = 1
#   for i in range(1,n+1):
#     productnum *= i
#   print(productnum)
# product(3)

# question 4 using recursion 
# def product(n):
#   if n == 0:
#     return 1
#   return n * product(n-1)

# print(product(4))

# 5.  Print numbers from 1 to N and N to 1
# def printns(n):
#   for i in range(n+1):
#     print(i,end="-")
#     print(n-i)
# printns(8)    

#Q5 with recursion 
def ascending_nums(i,n):
  if i>n:
    return 0
  print(i)
  
  return ascending_nums(i+1,n)
ascending_nums(1,8)