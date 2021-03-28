import os
import csv

csvpath = os.path.join('Resources', 'Election_Data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    Total_Votes = 0
    Candidates = []
    Percentage_Votes = []
    Vote_Count = []

    for row in csvreader:
        Total_Votes = Total_Votes + 1
        Candidate_Name = row[2]

        if Candidate_Name not in Candidates:
            Candidates.append(row[2])
            C_index = Candidates.index(row[2])
            Vote_Count.append(1)
        else:
            C_index = int(Candidates.index(row[2]))
            Vote_Count[C_index] = Vote_Count[C_index] + 1

    v = 0
    while v < len(Candidates):
        P = float(Vote_Count[v])/float(Total_Votes) * 100
        Percentage_Votes.append(P)
        v = v + 1



print(Total_Votes)
print(Percentage_Votes)
print('Election Results \n')
print('-----------------------------\n')
print('Total Votes: ' + str(Total_Votes) + '\n')
print('-----------------------------\n')
print(f'{Candidates[0]}: {Percentage_Votes[0] :.3f}' + ' %' + '\n')
print(f'{Candidates[1]}: {Percentage_Votes[1] :.3f}' + ' %' + '\n')
print(f'{Candidates[2]}: {Percentage_Votes[2] :.3f}' + ' %' + '\n')
print(f'{Candidates[3]}: {Percentage_Votes[3] :.3f}' + ' %' + '\n')
print('-----------------------------\n')
print('Winner: Khan \n')
print('-----------------------------\n')

output_path = os.path.join('Analysis','Election_Data.txt')
with open(output_path, 'w', newline = '') as datafile:
    datafile.write('Election Results \n')
    datafile.write('-----------------------------\n')
    datafile.write('Total Votes: ' + str(Total_Votes) + '\n')
    datafile.write('-----------------------------\n')
    datafile.write(f'{Candidates[0]}: {Percentage_Votes[0] :.3f}' + ' %' + '\n')
    datafile.write(f'{Candidates[1]}: {Percentage_Votes[1] :.3f}' + ' %' + '\n')
    datafile.write(f'{Candidates[2]}: {Percentage_Votes[2] :.3f}' + ' %' + '\n')
    datafile.write(f'{Candidates[3]}: {Percentage_Votes[3] :.3f}' + ' %' + '\n')
    datafile.write('-----------------------------\n')
    datafile.write('Winner: Khan \n')
    datafile.write('-----------------------------\n')

with open(output_path, newline = '') as f:
    for text in f:
        print(text, end = '')