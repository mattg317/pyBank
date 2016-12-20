import csv

file_input = "raw_data/budget_data_1.csv"
file_output = "raw_data/results.txt"

#Default variable for what we are looking for
total_months = 0
total_rev = 0
prev_rev = 0
month_of_change = []
rev_change_list = []
biggest_decr = ['', 9999999999999999999999999999]
biggest_incr = ['', 0]

with open(file_input) as rev_data:
    reader = csv.DictReader(rev_data)
    for row in reader:

        total_months += 1
        total_rev += int(row['Revenue'])

        rev_change = int(row["Revenue"])- prev_rev
        prev_rev = int(row["Revenue"])
        rev_change_list = rev_change_list + [rev_change]
        month_of_change = month_of_change + [row["Date"]]

        if rev_change>biggest_incr[1]:
            biggest_incr[1]= rev_change
            biggest_incr[0] = row['Date']

        if rev_change<biggest_decr[1]:
            biggest_decr[1]= rev_change
            biggest_decr[0] = row['Date']

print(biggest_incr)
print(biggest_decr)

#print(rev_change_list)
rev_avg = sum(rev_change_list)/len(rev_change_list)


print('Average change in revenue is $%d' % rev_avg)
print("Total months is %s" % total_months)
print("The total revenue is $%d" % total_rev)

with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_rev)
    file.write("Average Revenue Change $%d\n" % rev_avg)
    file.write("Greatest Increase in Revenue: %s ($%d)\n" % (biggest_incr[0], biggest_incr[1]))
    file.write("Greatest Decrease in Revenue: %s ($%d)\n" % (biggest_decr[0], biggest_decr[1]))
