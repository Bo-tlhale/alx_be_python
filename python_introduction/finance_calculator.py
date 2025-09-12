monthlyIncome = float(input("Enter your monthly income: "))
monthlyExpenses = float(input("Enter your total monthly expenses: "))
monthlySavings = monthlyIncome - monthlyExpenses
rate = 0.05
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * rate)
print("Your monthly savings are $" + str(monthlySavings))
print("Projected savings after one year, with interest, is: $" + str(projectedSavings))