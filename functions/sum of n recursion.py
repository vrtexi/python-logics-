# WAP A RECURSIVE FUNCTIONN TO CALCULATE THE SUM OF THE FIRST N NATURAL NUMBERS 

def sum(n):
  if n == 0:
    return 0
  return sum(n-1) + n
print(sum(2))