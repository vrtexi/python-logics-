# Validate user input exercise 
# 1.  Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Whats your Username? : ")

if  len(username) > 12:
  print("Your username must be in 12 digits")
elif not username.find(" ") == -1:
  print("Your username must not contain spaces")
elif not username.isalpha():
  print("Your username must not contain digits")
else:
  print(f"Welcome {username}")