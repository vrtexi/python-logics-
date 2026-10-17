# Find largest and smallest element
a = [50,23,12,9,100]
max_num=a[0]
min_num = a[0]
for  i in a:
  if i > max_num:
    max_num = i
  if i <= min_num:
    min_num = i
print(max_num)
print(min_num)

# Logic to remember: initialize both with the first element, then compare every element against them.