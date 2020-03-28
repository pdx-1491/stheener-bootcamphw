import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # for row in csvreader:
    # print(row)

print('Election Results')
print('-----------------------')
# print('Total votes:')
print('-----------------------')
# print('Khan: ')
# print('Correy: ')
# print('Li: ')
# print("O'Tooley: ")
print('-----------------------')
# print('Winner: ')
print('-----------------------')
