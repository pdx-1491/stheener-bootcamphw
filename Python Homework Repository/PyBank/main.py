import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv')

month_count = 0
net_total = 0
current_value = 0
total_net_change = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # for row in csvreader:
    #   print(row)

    for row in csvreader:
        month_count = month_count + 1
        net_total += int(row[1])
        current_value += int(row[1]) + int(row[1])
        total_net_change = int(row[1]) - current_value

print(current_value)
print('Financial Analysis')
print('------------------------')
print('Total Months: ' + str(month_count))
print("Total: " + '$' + str(net_total))
print("Average Change: " + '$' + str(total_net_change))
# print("Greatest Increase in Profits: " + '$' + month_variable + amount_variable)
# print("Greatest Decrease in Profits: " + '$' + month_variable + amount_variable)
