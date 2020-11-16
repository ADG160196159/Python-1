def poundstodollarconv():
  money_pounds = int(input("How much money do you have in pounds?")) #asking user to input how much money they have in pounds
  poundstodollar = money_pounds * 1.29 #Creating a new variable that takes the input of the previous question and times it but 1.29 to get the amount in USD
  print("You have", poundstodollar, "in USD") #Print the coverted amount from Pounds to USA
  if poundstodollar >= 100: #Checks if the amount you have is 100 or more
    print("You have a bit of money there") #Print this statement if you have more than 100USD
  else:
    print("You dont have alot of money there") #Print this statement if you have less than 100USD

def somethingelse():
  l = "There is nothing here yet"
  print(l)

poundstodollarconv()