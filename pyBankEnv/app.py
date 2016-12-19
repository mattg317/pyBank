import csv

#convert CSV file to a List
with open("raw_data/budget_data_1.csv", 'r') as f:
	reader = csv.reader(f)
	bank_data = list(reader)
del bank_data[0] #delete text at start

#Print total months recorded with is lenght of the list
totalMonths = len(bank_data)
print("Total Months:",totalMonths)

#total revenue is the sum of every recorded revenue for the month
total = 0
for i in range(len(bank_data)):
	total +=int(bank_data[i][1])

print("Total Revene: $%d" % total)

#First we get the change in revenue between all the months
revenueChange = []
for i in range(len(bank_data)):
	if i != len(bank_data)-1:
		change =int(bank_data[i][1])- int(bank_data[i+1][1])
		revenueChange.append(change)

#then we add the total amount of changes then divide but total length
total =0
for i in range(len(revenueChange)):
	total += revenueChange[i]

total = total/len(revenueChange)
print("Average Revenue Change $%d" %total)

# find greatest and lowest change in  Revenue

# for i in range(len(bank_data)):
# 	low = bank_data[i][0]
# 	high = bank_data[i][0]
# 	if revenueChange[i] < low:
# 		low = revenueChange[i]
# 	elif revenueChange[i] > high:
# 		high = revenueChange[i] 
# print("Greatest Increase in Revenue: %d" % high)
# print("Greatest Decrese in Revenue: %d" % low)