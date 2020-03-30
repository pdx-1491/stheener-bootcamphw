import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

# the total amount of rows aka "votes" in the csv
total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = len(list(csvreader))

    # for row in csvreader:
    # total_votes += int(row[0])

print('Election Results')
print('-----------------------')
print('Total votes: ' + str(total_votes))
print('-----------------------')
# print('Khan: ')
# print('Correy: ')
# print('Li: ')
# print("O'Tooley: ")
print('-----------------------')
# print('Winner: ')
print('-----------------------')
