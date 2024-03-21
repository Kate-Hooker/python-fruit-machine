MAX_LINES = 3

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
# deposit()
    
# USER INPUT - this allows the user to enter the number of lines they want to bet on
def get_number_of_lines():
  while True:
    lines = input("How many lines would you like to bet on? (1-" + str(MAX_LINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines >= MAX_LINES:
        break
      else:
        print("Please enter a valid number of lines")
        break

    else:
      print("Please enter a number")

      return lines


# MAIN FUNCTION: this can be called over and over again until credit runs out or the user quits

def main():
  balance = deposit()


# CALL THE FUNCTION - this function contains the game
  main()
