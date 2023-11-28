print("Tip Calculator")
billAmount = float(input("How much did you spend? "))
tipPercentage = int(input("What percentage you want to tip? "))
tipAmount = float(billAmount * tipPercentage/100)
print("tip amount is ", tipAmount)
totalSpent = float(billAmount + tipAmount)
print("Total amount spent is ", totalSpent)
numberOfPeople = int(input("How many people in your group? "))
eachOwe = totalSpent / numberOfPeople
print("You each owe ", eachOwe)
eachOwe = round(eachOwe, 2)
print("You each owe ", eachOwe)

