# wap to get the string palindrome using slices

a = input("Enter yr string: ")

new_String = a[-1::-1]
if a == new_String:
  print("true")
  
else:
  print("false")