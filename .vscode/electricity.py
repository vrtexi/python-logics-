unit = int(input("Enter the unit of electricity: "))
bill = 0
if unit <= 100:
  bill = unit * 5
elif unit > 100 and unit <= 300:
  bill = unit *5.5
else:
  bill = unit*6.5

bill = bill + 1000
if bill > 3000:
  bill = bill - (0.1*bill)
print(bill)

