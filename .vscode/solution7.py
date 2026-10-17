# Take a number from the user and print its table.

# Example:
# 5 × 1 = 5
# 5 × 2 = 10
# ...
# 5 × 10 = 50

num = int(input("Enter the num: "))
i=1
while i <=10:
  res =num *i
  
  print(f"{num}X{i} = {res:02}")
  i=i+1