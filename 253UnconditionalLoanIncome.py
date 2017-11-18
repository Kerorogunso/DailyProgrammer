import pandas as pd

def calculate_loan(interest,loan,age,incomes,clawback):
	column_names = ['loan','income','age','clawback','royalty','before','after']
	myTable = pd.DataFrame(columns=column_names)
	f = lambda x: 0.4 if x > 65 else 0.2 # Clawback age
	g = lambda y: 1 if y > 100 else 0 # Clawback threshold
	outstanding = 0
	current_age = age

	for income in incomes:
		before = outstanding * (1 + interest) + loan
		clawback = f(current_age) * loan * g(outstanding)
		royalty = f(current_age) * income
		outstanding = before - (clawback + royalty)
		row = pd.DataFrame([[loan,income,current_age,clawback,royalty,before,outstanding]],columns=column_names)
		myTable = myTable.append(row)
		current_age += 1

	return myTable

my_incomes = [0,0,20,20,20,20,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,0,0,0,0,0,0,0,0,0,0,0]

print(calculate_loan(0.02,15,18,my_incomes,100))



