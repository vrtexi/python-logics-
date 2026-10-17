import random


def spin_row():
  symbols= ['🍒', '🔔', '🍉' ,'🍋' ,'⭐']
  
  return [random.choice(symbols) for _ in range(3)]


def print_row(row):
  print(" | ".join(row))

def get_payout(row,bet):
  if row[0] == row[1] == row[2]:  
    if row[0] == '🍒':
      return bet*3
    elif row[0]=="🍉":
      return bet *6
    elif row[0] == '🔔':
      return bet *9
    elif row[0] == '🍋':
      return bet *12
    elif row[0] == '⭐':
      return bet *20
  return 0

def main():
  balance = 100
  
  print("Welcome to the PySlots")
  print("Symbols: 🍒 🔔 🍉 🍋 ⭐")

  while balance>0:
    print(f"current balance: ${balance:02}")
    
    bet = input("Enter an amount to place the bet: ")
    if not bet.isdigit():
      print("Please enter a valid number: ")
      continue
    
    bet = int(bet)
    
    if bet> balance:
      print("Insufficient funds") 
      continue
    
    if bet <=0:
      print("Bet must be greater than 0")
      continue
    
    balance -= bet
    
      
    row = spin_row()
    print("Spining....\n") 
    
    print_row(row)
    
    payout = get_payout(row, bet)
    
    if payout >0:
      print(f"You won ${payout}")
    else:
      print("Sorry you lost the program")
    
    balance += payout
    
    play_again = input("Do you wanna pplay again(Y/N): ").upper()
    if play_again != 'Y':
      break
    
  print(f"Game over! Final balance is ${balance}")
if __name__=='__main__':
  main()