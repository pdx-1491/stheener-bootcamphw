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

# keeps track of the 'profit/losses' difference between iterations in for loop
net_change = 0

# keeps track of single value when comparing profits to each other in 'profit/losses'
profit_change = 867884

# the largest increase in profit and the associated month
greatest_profit = 0
greatest_increase_date = ' '

# keeps track of single value when comparing losses to each other in 'profit/losses'
loss_change = 867884

# the largest decrease in profit and the associated month
greatest_loss = 0
greatest_decrease_date = ' '

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
        profit_change = net_change
        if profit_change > greatest_profit:
            greatest_profit = profit_change
            greatest_increase_date = str(row[0])

        # bullet 5 - greatest loss in profits with month
        loss_change = net_change
        if loss_change < greatest_loss:
            greatest_loss = loss_change
            greatest_decrease_date = str(row[0])

print('Financial Analysis')
print('------------------------')
print('Total Months: ' + str(month_count))
print("Total: " + '$' + str(net_total))
print("Average Change: " + '$' +
      str(round(total_net_change / (month_count - 1), 2)))
print("Greatest Increase in Profits: "
      + greatest_increase_date + ' ' + '(' + '$' + str(greatest_profit) + ')')
print("Greatest Increase in Profits: "
      + greatest_decrease_date + ' ' + '(' + '$' + str(greatest_loss) + ')')

# printing a csv
output_path = os.path.join('Analysis', 'results.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Total Months: ' + str(month_count)])
    csvwriter.writerow(["Total: " + '$' + str(net_total)])
    csvwriter.writerow(["Average Change: " + '$' +
                        str(round(total_net_change / (month_count - 1), 2))])
    csvwriter.writerow(["Greatest Increase in Profits: "
                        + greatest_increase_date + ' ' + '(' + '$' + str(greatest_profit) + ')'])
    csvwriter.writerow(["Greatest Increase in Profits: "
                        + greatest_decrease_date + ' ' + '(' + '$' + str(greatest_loss) + ')'])
