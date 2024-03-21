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
