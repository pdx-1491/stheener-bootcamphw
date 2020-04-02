import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

# the total amount of rows aka "votes" in the csv
votes = []

# the unique candidates in csv
candidates = []

# the aggregated votes for each candidate
candidate_votes = {}

# percentage of the vote total that each candidate received
candidate_percentages = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # bullet 1 - total number of votes cast
    for row in csvreader:
        votes.append(row[2])

        # bullet 2 - complete list of candidates who received votes
        # bullet 3 - percentage of votes each candidate won
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

# bullet 4 - total number of votes each candidate won
for name in candidate_votes:
    calculate_percentage = round(candidate_votes[name]/len(votes)*100, 3)
    candidate_percentages[name] = calculate_percentage

    # bullet 5 - winner of the election based on popular vote
    most_votes = max(candidate_votes, key=candidate_votes.get)

print('Election Results')
print('-----------------------')
print('Total votes: ' + str(len(votes)))
print('-----------------------')
print(candidates[0] + ':' + ' ' + str(candidate_percentages['Khan'])
      + ' ' + '(' + str(candidate_votes['Khan']) + ')')
print(candidates[1] + ':' + ' ' + str(candidate_percentages['Correy'])
      + ' ' + '(' + str(candidate_votes['Correy']) + ')')
print(candidates[2] + ':' + ' ' + str(candidate_percentages['Li'])
      + ' ' + '(' + str(candidate_votes['Li']) + ')')
print(candidates[3] + ':' + ' ' + str(candidate_percentages["O'Tooley"])
      + ' ' + '(' + str(candidate_votes["O'Tooley"]) + ')')
print('-----------------------')
print('Winner: ' + str(most_votes))
print('-----------------------')

# printing a csv
output_path = os.path.join('Analysis', 'results.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Total votes: ' + str(len(votes))])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow([candidates[0] + ':' + ' ' + str(candidate_percentages['Khan'])
                        + ' ' + '(' + str(candidate_votes['Khan']) + ')'])
    csvwriter.writerow([candidates[1] + ':' + ' ' + str(candidate_percentages['Correy'])
                        + ' ' + '(' + str(candidate_votes['Correy']) + ')'])
    csvwriter.writerow([candidates[2] + ':' + ' ' + str(candidate_percentages['Li'])
                        + ' ' + '(' + str(candidate_votes['Li']) + ')'])
    csvwriter.writerow([candidates[3] + ':' + ' ' + str(candidate_percentages["O'Tooley"])
                        + ' ' + '(' + str(candidate_votes["O'Tooley"]) + ')'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Winner: ' + str(most_votes)])
    csvwriter.writerow(['-----------------------'])
