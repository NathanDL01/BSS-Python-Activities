mealPrice=eval(input("How much is the meal? "))
tipPercent=eval(input("Tip Percentage: "))

tipAmount=mealPrice*(tipPercent/100)
total=mealPrice+tipAmount

print("The price for the tip is ", tipAmount, " Making your total payment to be ", total, ".",sep="")