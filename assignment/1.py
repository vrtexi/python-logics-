# Mobile Recharge Billing System

# Recharge amount up to ₹500 → No additional charge
# Recharge amount above ₹500 → 5% service charge

#  A fixed processing fee of ₹20 is applicable to every transaction

#  If the recharge amount exceeds ₹2000, an additional 3% service charge is applied. 

recharge_amount = int(input("Enter Your Recharge amount: "))
fpf = 20
service_charge5 = recharge_amount * 1/20
service_charge3 = recharge_amount * 0.03
if recharge_amount <= 0:
  print("Enter a valid number")
elif recharge_amount <= 500:
  print(f"Your Payable amount is: {recharge_amount + fpf} ")
elif recharge_amount > 500:
  print(f"Your Payable amount is: {recharge_amount + service_charge5 +fpf}")
elif recharge_amount > 2000:
  print(f"Your Payable amount is: {recharge_amount + service_charge5 + service_charge3 +fpf}")
  
