# Q2. Check whether a number is present in a list

# Given:

# numbers = [4, 8, 12, 17, 23, 31]
# Input a number from the user and check whether it exists in the list.

# Don't use in yet. Use a loop.

numbers = [4, 8, 12, 17, 23, 31]
user_input = int(input("Enter a number to check: "))

found = False
for i in numbers:
  if user_input == i:
    found = True
if found:
  print("in the list")
else:
  print("not in the list")