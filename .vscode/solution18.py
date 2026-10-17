# write a program to input username and password. if both are correct then display login succesfull

real_user = 'Aman123@'
real_pass = 'Admin@123'

user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")

is_loging = True
while is_loging:
  if user_name == real_user:
    print("correct user")
    if pass_word == real_pass:
      print("Correct password! Succesfully logged in.")
      is_loging = False
    else:
      print("Wrong password")
      pass_word = input("Wrong pass word reEnter your password: ")
  else:
    print("Wrong username! ")
    user_name = input("Wrong pass word reEnter your username: ")