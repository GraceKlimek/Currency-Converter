# This function converts USD to Euros and Euros
# to USD based on the name USD, Euro, or the symbols for USD and Euro.
def convert_currency(money):

  # Looks for Euro Symbol. When Detected, converts number inputted to USD.
  if "€" in money:
    #Removes the symbol from input,
    #takes the number and converts it to the USD Value.
    USD = float(money.strip("€")) * 1.07
    print("your money in USD is", USD)
# looks for the word euro. When it is detected it convers the number inputted to USD.
  elif "euro" in money:
    USD = float(money.strip("euros")) * 1.07
    print("Your money in USD is:", USD)
# looks for the USD symbol ($). When detected, converts number to euros.
  elif "$" in money:
    # strip removed the symbol from the input 
    # takes the number and converts it to the Euro value.
    euro = float(money.strip("$")) * 0.93
    print("Your money in euros is:", euro)
# looks for the word USD. When detected, converts number to euros.
  elif "usd" in money:
    euro = float(money.strip("usd")) * 0.93
    print(" your money in euro is", euro)
#if any other currency is entered it responds with message below.
  else:
    print("Please enter a valid currency")


print("Hello, please enter the amount of money you want to convert\n"
      "from Euros->USD or USD->Euros:")

# Takes the users input. Converts text to all lowercase letters.
# Removes whitespace.
money = input().lower().strip()

# Looks for negative numbers. If none are seen, convert the money.
if "-" not in money:
  convert_currency(money)
#Tell User negative numbers are not allowed.
else:
  print("you must enter a positive number")

