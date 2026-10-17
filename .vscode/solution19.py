# input two strings. if string one contained in string two ,then create thrid string with first four characters  of string two added with the word "restore" 

string1 = input("Enter the string first: ")
string2 = input("Enter the second string: ")

# string3 = [ string2[:4] + "restore" for _ in string2  if string1 in string2 ]

# print(string3)


if string1 in string2:
  string3= string2[:4] + "restore"
  print(string3)