year = int(input("Enter a valid year: "))

if year <9999:
  if year % 4==0:
    print("leap year")
  else:
    print("not a leap year")
else:
  print("Enter a valid year") 
  year = int(input("Renter a valid year: "))
  