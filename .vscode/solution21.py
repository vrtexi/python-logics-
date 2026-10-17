admin = 'Admin123'
emp = 'Employee'
ad_pass='Admin123@'

user = input("Enter Username :")
is_real = True
while is_real:
  if(user == admin):
    print("Admin...")
    pass1 = input("Enter Password: ")
    if(pass1 == ad_pass):
      print("Admin Login Succesfull: ")
      is_real = False
    else:
         print("Wrong Password.")
         pass1 = input("Enter Password.")
  elif(user == emp) :
    print("Login Succesfull.")
    break
  else :
    print("Wrong username.")
    user = input("Enter Username :")
      
