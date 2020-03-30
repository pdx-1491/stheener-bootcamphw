import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv')

# totaling the number of months in the csv
month_count = 0

# totaling the 'profit/losses' column in csv
net_total = 0

# the starting value in 'profit/losses' column
current_value = 867884

# keeps track of running total when comparing each value to each other in 'profi/losses'
total_net_change = 0

# net_change
net_change = 0

# keeps track of single value when comparing profits to each other in 'profit/losses'
profit_change = 0

# the largest increase in profit month over month
greatest_increase = 867884
greatest_increase_date = " "

#starting_value = int(row[1])
#next_value = int(row[1]) + 1
#running_value = 0

# keeps track of single value when comparing losses to each other in 'profit/losses'
loss_change = 0

# the largest decrease in profit month over month
loss_largest = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # bullet 1 - total number of months
        month_count = month_count + 1

        # bullet 2 - net total amount
        net_total += int(row[1])

        # bullet 3 - average change in 'profit/losses'
        net_change = int(row[1]) - current_value
        total_net_change += net_change
        current_value = int(row[1])

        # bullet 4 - greatest increase in profits with month
        print("net change = " + str(net_change))
        print("greatest increase = " + str(greatest_increase))

        if net_change > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increse_date = str(row[0])

            print("\ngreatest increase = " + str(greatest_increase))
            print("greatest increase date = " + str(greatest_increase_date))

        # bullet 5 - greatest decrease in profits with month
        # net_change = int(row[1]) - current_value

print(greatest_increase)
print(greatest_increse_date)

'''
def is_profitable(x, y):
    profit = y - x
    if (profit > 0):
        return profit
'''

print('Financial Analysis')
print('------------------------')
print('Total Months: ' + str(month_count))
print("Total: " + '$' + str(net_total))
print("Average Change: " + '$' +
      str(round(total_net_change / (month_count - 1), 2)))
# print("Greatest Increase in Profits: " + '$' + month_variable + amount_variable)
# print("Greatest Decrease in Profits: " + '$' + month_variable + amount_variable)
