def deposit():
  while True:
    amount = input("Enter amount to deposit: $")
    if amount.isdigit():
      amount = int(amount)
