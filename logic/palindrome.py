# Q24 — Palindrome number

# Input:

# 121

# Output:

# Palindrome

# But:

# 123

# →

# Not palindrome

# Think:

# What relationship exists between a number and its reverse?


num = int(input("Enter a number: "))
temp = num
rev=0
while True:
  if num == 0:
    break
  r = num %10
  num = num //10
  rev = rev*10+r

  # if 
  