# DEPOSIT FUNCTION - this is a while loop that will only break and return once a real amount has been put into the fruit machine so game play can commence
def deposit():
  while True:
    amount = input("Enter amount to deposit: $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Please pick an amount bigger than zero")
    else:
      print("Please enter a number")

      return amount

# CALL THE FUNCTION - this begins the while loop to start the game
deposit()

