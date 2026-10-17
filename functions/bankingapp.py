def withdraw():
  withdraw_amount = int(input("Enter the amount to withdraw: "))
  return withdraw_amount
  
def deposit():
  deposit_amount = int(input("Enter the amount to deposit: "))
  return deposit_amount

def showBalance():
  print(f"Your Balance is {balance} ")

def exit():
  pass

balance = 0
isRunning = True

while isRunning:
  print('''
        1 = Withdraw
        2 = Deposit
        3 = Balance
        4 = Exit:''')
  choice= int(input("What Would You Like To Do "))
  if choice == 1:
    balance -= withdraw()
  elif choice == 2:
    balance +=deposit()
  elif choice == 3: 
    showBalance()
  elif choice ==4:
    isRunning = False
  else:
    print("Retry")
    
# if __name__ == '__main__':
#   main()

# enter some validation 